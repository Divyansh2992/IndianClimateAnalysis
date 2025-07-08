const fs = require('fs');
const path = require('path');
require('dotenv').config();

// Helper to create Google Drive direct download link from file ID
function getDriveDownloadUrl(fileId) {
    return `https://drive.google.com/uc?export=download&id=${fileId}`;
}

// Load BIN file mapping
const binFileIds = require('../file_mappings/binFileIds.json');
// Load EPW file mapping
const epwFileIds = require('../file_mappings/epwFileIds.json');

const csvFileIds=require('../file_mappings/csvFileIds.json');

// Middleware to resolve district name to Google Drive BIN file URL
function resolveBinByDistrict(req, res, next) {
    const district = req.params.district;
    let fileId = binFileIds[district];
    if (!fileId) {
        fileId = Object.entries(binFileIds).find(([key]) => typeof key === 'string' && typeof district === 'string' && key.toLowerCase() === district.toLowerCase())?.[1];
    }
    if (!fileId) {
        if (typeof district === 'string') {
            const normDistrict = district.replace(/\s+|_/g, '').toLowerCase();
            fileId = Object.entries(binFileIds).find(([key]) => typeof key === 'string' && key.replace(/\s+|_/g, '').toLowerCase() === normDistrict)?.[1];
        }
    }
    if (!fileId) {
        return res.status(404).json({ error: 'No BIN file found for district: ' + district });
    }
    req.binDriveUrl = getDriveDownloadUrl(fileId);
    next();
}

// Middleware to resolve district name to Google Drive EPW file URL
function resolveEpwByDistrict(req, res, next) {
    const district = req.params.district;
    let fileId, resolvedKey;
    fileId = epwFileIds[district];
    resolvedKey = district;
    if (!fileId) {
        const entry = Object.entries(epwFileIds).find(([key]) => typeof key === 'string' && typeof district === 'string' && key.toLowerCase() === district.toLowerCase());
        if (entry) {
            fileId = entry[1];
            resolvedKey = entry[0];
        }
    }
    if (!fileId) {
        if (typeof district === 'string') {
            const normDistrict = district.replace(/\s+|_/g, '').toLowerCase();
            const entry = Object.entries(epwFileIds).find(([key]) => typeof key === 'string' && key.replace(/\s+|_/g, '').toLowerCase() === normDistrict);
            if (entry) {
                fileId = entry[1];
                resolvedKey = entry[0];
            }
        }
    }
    if (!fileId) {
        return res.status(404).json({ error: 'No EPW file found for district: ' + district });
    }
    req.epwDriveUrl = getDriveDownloadUrl(fileId);
    req.epwResolvedFilename = resolvedKey;
    next();
}

// Middleware to resolve district name to Google Drive CSV file URL
function resolveCsvByDistrict(req, res, next) {
    const district = req.params.district;
    let fileId, resolvedKey;
    fileId = csvFileIds[district];
    resolvedKey = district;
    if (!fileId) {
        const entry = Object.entries(csvFileIds).find(([key]) => typeof key === 'string' && typeof district === 'string' && key.toLowerCase() === district.toLowerCase());
        if (entry) {
            fileId = entry[1];
            resolvedKey = entry[0];
        }
    }
    if (!fileId) {
        if (typeof district === 'string') {
            const normDistrict = district.replace(/\s+|_/g, '').toLowerCase();
            const entry = Object.entries(csvFileIds).find(([key]) => typeof key === 'string' && key.replace(/\s+|_/g, '').toLowerCase() === normDistrict);
            if (entry) {
                fileId = entry[1];
                resolvedKey = entry[0];
            }
        }
    }
    if (!fileId) {
        return res.status(404).json({ error: 'No CSV file found for district: ' + district });
    }
    req.csvDriveUrl = getDriveDownloadUrl(fileId);
    req.csvResolvedFilename = resolvedKey;
    next();
}

module.exports = { resolveBinByDistrict, resolveEpwByDistrict, resolveCsvByDistrict };
