const fs = require('fs');
const axios = require('axios');

// GET /api/epw/windv-monthwise/:filename - Return monthwise wind velocity arrays for plotting
exports.getWindVelocityMonthwise = async (req, res) => {
    const epwDriveUrl = req.epwDriveUrl;
    if (!epwDriveUrl) {
        return res.status(404).json({ error: 'EPW file not found for district' });
    }
    let data;
    try {
        const response = await axios.get(epwDriveUrl);
        data = response.data;
    } catch (err) {
        return res.status(404).json({ error: 'EPW file could not be downloaded' });
    }
    const lines = data.split(/\r?\n/).filter(Boolean);
    if (lines.length <= 8) {
        return res.status(400).json({ error: 'Invalid EPW file' });
    }
    const dataLines = lines.slice(8);
    const wv = [];
    for (const line of dataLines) {
        const cols = line.split(',');
        if (cols.length < 22) continue;
        wv.push(parseFloat(cols[21])); // Wind velocity (m/s) is column 22 (index 21)
    }
    const monthLengths = [744, 672, 744, 720, 744, 720, 744, 744, 720, 744, 720, 744];
    let start = 0;
    const wvMonth = [];
    for (let m = 0; m < 12; m++) {
        const end = start + monthLengths[m];
        wvMonth.push(wv.slice(start, end));
        start = end;
    }
    res.json({ wv: wvMonth });
};
