const fs = require('fs');
const path = require('path');

// Middleware to validate EPW filename and path
function validateEpwFilename(req, res, next) {
    const filename = req.params.filename;
    const epwDir = path.join(__dirname, '../epw_files');
    const filePath = path.join(epwDir, filename);
    if (!filePath.startsWith(epwDir)) {
        return res.status(400).json({ error: 'Invalid filename' });
    }
    req.epwFilePath = filePath;
    next();
}


// Mapping function: district name to EPW filename
function getEpwFilenameFromDistrict(district) {
    // List all files in epw_files directory
    const epwDir = path.join(__dirname, '../epw_files');
    const files = fs.readdirSync(epwDir);
    // Try to find a file that includes the district name (case-insensitive, ignoring spaces)
    const normalizedDistrict = district.replace(/\s+/g, '').toLowerCase();
    const match = files.find(f => f.replace(/\s+/g, '').toLowerCase().includes(normalizedDistrict));
    return match || null;
}

// Middleware to allow district name as filename
function resolveEpwByDistrict(req, res, next) {
    const district = req.params.district;
    const filename = getEpwFilenameFromDistrict(district);
    if (!filename) {
        return res.status(404).json({ error: 'No EPW file found for district: ' + district });
    }
    req.epwFilePath = path.join(__dirname, '../epw_files', filename);
    req.epwResolvedFilename = filename;
    next();
}

module.exports = { validateEpwFilename, resolveEpwByDistrict };
