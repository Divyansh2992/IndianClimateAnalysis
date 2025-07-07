const fs = require('fs');

// GET /api/epw/radiation-monthwise/:filename - Return monthwise radiation arrays for plotting (nonzero only)
exports.getRadiationMonthwise = (req, res) => {
    const filePath = req.epwFilePath;
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(404).json({ error: 'File not found' });
        }
        const lines = data.split(/\r?\n/).filter(Boolean);
        if (lines.length <= 8) {
            return res.status(400).json({ error: 'Invalid EPW file' });
        }
        const dataLines = lines.slice(8);
        const ghr = [], dnr = [], dhr = [];
        for (const line of dataLines) {
            const cols = line.split(',');
            if (cols.length < 22) continue;
            ghr.push(parseFloat(cols[13]));  // Global horizontal radiation (Wh/m2)
            dnr.push(parseFloat(cols[14]));  // Direct normal radiation (Wh/m2)
            dhr.push(parseFloat(cols[15]));  // Diffuse horizontal radiation (Wh/m2)
        }
        const monthLengths = [744, 672, 744, 720, 744, 720, 744, 744, 720, 744, 720, 744];
        let start = 0;
        function monthwiseNonZero(arr) {
            let out = [];
            let idx = 0;
            for (let m = 0; m < 12; m++) {
                const end = start + monthLengths[m];
                const monthArr = arr.slice(start, end).filter(v => v !== 0);
                out.push(monthArr);
                start = end;
            }
            start = 0; // reset for next array
            return out;
        }
        const ghrMonth = monthwiseNonZero(ghr);
        const dnrMonth = monthwiseNonZero(dnr);
        const dhrMonth = monthwiseNonZero(dhr);
        res.json({ ghr: ghrMonth, dnr: dnrMonth, dhr: dhrMonth });
    });
};
