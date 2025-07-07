const fs = require('fs');
const path = require('path');
const fetch = require('node-fetch');

// GET /api/epw/:filename - Return raw EPW file content
exports.getEpwFile = (req, res) => {
    fs.readFile(req.epwFilePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(404).json({ error: 'File not found' });
        }
        res.json({ filename: req.params.filename, data });
    });
};

// Use the generated mapping files for file IDs
const epwFileIds = require('../file_mappings/epwFileIds.json');
const csvFileIds = require('../file_mappings/csvFileIds.json');
const binFileIds = require('../file_mappings/binFileIds.json');

function getDriveDownloadUrl(fileId) {
  return `https://drive.google.com/uc?export=download&id=${fileId}`;
}

// Download EPW file for a given district from Google Drive
exports.downloadEpwFile = async (req, res) => {
  const district = req.params.district;
  const fileId = epwFileIds[district];
  if (!fileId) {
    return res.status(404).json({ error: 'EPW file not found for this district' });
  }
  const downloadUrl = getDriveDownloadUrl(fileId);
  try {
    const response = await fetch(downloadUrl);
    if (!response.ok) throw new Error('Download failed');
    res.setHeader('Content-Disposition', `attachment; filename="${district}.epw"`);
    response.body.pipe(res);
  } catch (err) {
    res.status(404).json({ error: 'EPW file not found or could not be downloaded' });
  }
};

// Download CSV file for a given district from Google Drive
exports.downloadCsvFile = async (req, res) => {
  const district = req.params.district;
  const fileId = csvFileIds[district];
  if (!fileId) {
    return res.status(404).json({ error: 'CSV file not found for this district' });
  }
  const downloadUrl = getDriveDownloadUrl(fileId);
  try {
    const response = await fetch(downloadUrl);
    if (!response.ok) throw new Error('Download failed');
    res.setHeader('Content-Disposition', `attachment; filename="${district}.csv"`);
    response.body.pipe(res);
  } catch (err) {
    res.status(404).json({ error: 'CSV file not found or could not be downloaded' });
  }
};

// Download BIN file for a given district from Google Drive
exports.downloadBinFile = async (req, res) => {
  const district = req.params.district;
  const fileId = binFileIds[district];
  if (!fileId) {
    return res.status(404).json({ error: 'BIN file not found for this district' });
  }
  const downloadUrl = getDriveDownloadUrl(fileId);
  try {
    const response = await fetch(downloadUrl);
    if (!response.ok) throw new Error('Download failed');
    res.setHeader('Content-Disposition', `attachment; filename="${district}.bin"`);
    response.body.pipe(res);
  } catch (err) {
    res.status(404).json({ error: 'BIN file not found or could not be downloaded' });
  }
};






