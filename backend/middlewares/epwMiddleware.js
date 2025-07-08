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

// Middleware to resolve district name to Google Drive BIN file URL
function resolveBinByDistrict(req, res, next) {
    const district = req.params.district;
    // Try exact match, then case-insensitive, then normalized (replace spaces/underscores)
    let fileId = binFileIds[district];
    if (!fileId) {
        // Try case-insensitive
        fileId = Object.entries(binFileIds).find(([key]) => key.toLowerCase() === district.toLowerCase())?.[1];
    }
    if (!fileId) {
        // Try normalized
        const normDistrict = district.replace(/\s+|_/g, '').toLowerCase();
        fileId = Object.entries(binFileIds).find(([key]) => key.replace(/\s+|_/g, '').toLowerCase() === normDistrict)?.[1];
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
        const entry = Object.entries(epwFileIds).find(([key]) => key.toLowerCase() === district.toLowerCase());
        if (entry) {
            fileId = entry[1];
            resolvedKey = entry[0];
        }
    }
    if (!fileId) {
        const normDistrict = district.replace(/\s+|_/g, '').toLowerCase();
        const entry = Object.entries(epwFileIds).find(([key]) => key.replace(/\s+|_/g, '').toLowerCase() === normDistrict);
        if (entry) {
            fileId = entry[1];
            resolvedKey = entry[0];
        }
    }
    if (!fileId) {
        return res.status(404).json({ error: 'No EPW file found for district: ' + district });
    }
    req.epwDriveUrl = getDriveDownloadUrl(fileId);
    req.epwResolvedFilename = resolvedKey;
    next();
}

module.exports = { resolveBinByDistrict, resolveEpwByDistrict };
