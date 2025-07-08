const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');
const axios = require('axios');

// POST /api/epw/psychrometry/save-svg
exports.savePsychrometrySVG = async (req, res) => {
    const params = req.body;
    const district = params.district;
    if (!district) {
        return res.status(400).send('District is required');
    }
    // Use Google Drive URL from middleware
    const epwDriveUrl = req.epwDriveUrl;
    if (!epwDriveUrl) {
        return res.status(404).send('EPW file not found for district');
    }
    let epwDataRaw;
    try {
        const response = await axios.get(epwDriveUrl);
        epwDataRaw = response.data;
    } catch (err) {
        return res.status(404).send('EPW file could not be downloaded');
    }
    const epwData = epwDataRaw.split(/\r?\n/);
    const header = epwData[0].split(',');
    const elevation = parseFloat(header[9]);
    const dbt = [], rh = [];
    for (let i = 8; i < epwData.length; i++) {
        const cols = epwData[i].split(',');
        if (cols.length > 8) {
            dbt.push(parseFloat(cols[6]));
            rh.push(parseFloat(cols[8]));
        }
    }
    // Get time range from params
    const fromMonth = params.fromMonth || 'January';
    const toMonth = params.toMonth || 'December';
    const fromDay = params.fromDay || 1;
    const toDay = params.toDay || 31;
    const fromHour = params.fromHour || 1;
    const toHour = params.toHour || 24;

    // Map month names to indices (EPW: Jan=1, ..., Dec=12)
    const monthMap = {
      'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
      'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    };
    const fromMonthIdx = monthMap[fromMonth];
    const toMonthIdx = monthMap[toMonth];

    // Filter dbt/rh by time range
    const filtered_dbt = [];
    const filtered_rh = [];
    for (let i = 8; i < epwData.length; i++) {
        const cols = epwData[i].split(',');
        if (cols.length > 8) {
            const month = parseInt(cols[1]);
            const day = parseInt(cols[2]);
            const hour = parseInt(cols[3]);
            // Check if within selected range
            const inMonth = (fromMonthIdx <= toMonthIdx)
                ? (month >= fromMonthIdx && month <= toMonthIdx)
                : (month >= fromMonthIdx || month <= toMonthIdx); // wrap-around
            const inDay = (day >= fromDay && day <= toDay);
            const inHour = (hour >= fromHour && hour <= toHour);
            if (inMonth && inDay && inHour) {
                filtered_dbt.push(parseFloat(cols[6]));
                filtered_rh.push(parseFloat(cols[8]));
            }
        }
    }
    // Write dbt, rh, elevation, and other params to a temp file
    const tempDir = os.tmpdir();
    const tempInputPath = path.join(tempDir, `psycho_input_${Date.now()}.json`);
    const inputData = {
      dbt: filtered_dbt,
      rh: filtered_rh,
      elevation,
      text: params.text || "0 - 0.5 m/s",
      comf: typeof params.comf !== 'undefined' ? params.comf : 0,
      epw: typeof params.epw !== 'undefined' ? params.epw : 0,
      evap: typeof params.evap !== 'undefined' ? params.evap : 0,
      thm: typeof params.thm !== 'undefined' ? params.thm : 0,
      sun: typeof params.sun !== 'undefined' ? params.sun : 0,
      active: typeof params.active !== 'undefined' ? params.active : 0,
      possible_passive: typeof params.possible_passive !== 'undefined' ? params.possible_passive : 0,
      evap_efficiency: params.evap_efficiency || 100,
      fromMonth,
      toMonth,
      fromDay,
      toDay,
      fromHour,
      toHour
    };
    fs.writeFileSync(tempInputPath, JSON.stringify(inputData));
    // Now only pass the temp file path as an argument
    const scriptPath = path.join(__dirname, '../../python/passive_backend.py');
    const args = ['--input', tempInputPath];
    const pythonProcess = spawn('python', [scriptPath, ...args]);
    let svgData = '';
    pythonProcess.stdout.on('data', (data) => {
        svgData += data.toString();
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
    pythonProcess.on('close', (code) => {
        fs.unlinkSync(tempInputPath); // Clean up temp file
        if (code === 0) {
            res.set('Content-Type', 'image/svg+xml');
            res.send(svgData);
        } else {
            res.status(500).send('Error generating SVG');
        }
    });
};
