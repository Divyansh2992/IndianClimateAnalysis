const fs = require('fs');
const path = require('path');
const axios = require('axios');
const { spawn } = require('child_process');
const os = require('os');

// GET /api/epw/summary/:filename - Return weather summary
exports.getEpwSummary = async (req, res) => {
    console.log('Starting EPW summary calculation...');
    console.log('Reading EPW file:', req.epwFilePath);

    fs.readFile(req.epwFilePath, 'utf8', async (err, data) => {
        if (err) {
            console.error('Error reading EPW file:', err);
            return res.status(404).json({ error: 'File not found' });
        }

        console.log('Successfully read EPW file');
        const lines = data.split(/\r?\n/).filter(Boolean);
        if (lines.length <= 8) {
            console.error('Invalid EPW file: insufficient data lines');
            return res.status(400).json({ error: 'Invalid EPW file' });
        }

        console.log('Processing header data...');
        const dataLines = lines.slice(8);
        const dbt = [], rh = [], dpt = [], wbt = [], ghr = [], dnr = [], dhr = [], ghi = [], dni = [];

        // Extract values from data lines
        console.log('Extracting hourly data...');
        for (const line of dataLines) {
            const cols = line.split(',');
            if (cols.length < 22) continue;
            dbt.push(parseFloat(cols[6]));   // Dry bulb temperature (°C)
            dpt.push(parseFloat(cols[7]));   // Dew point temperature (°C)
            rh.push(parseFloat(cols[8]));    // Relative humidity (%)
            ghr.push(parseFloat(cols[13]));  // Global horizontal radiation (Wh/m2)
            dnr.push(parseFloat(cols[14]));  // Direct normal radiation (Wh/m2)
            dhr.push(parseFloat(cols[15]));  // Diffuse horizontal radiation (Wh/m2)
            dni.push(parseFloat(cols[16]));  // Direct normal illuminance (lux)
            ghi.push(parseFloat(cols[17]));  // Global horizontal illuminance (lux)
        }
        console.log(`Extracted ${dbt.length} hours of data`);
       
        // Get elevation from header
        let elevation = 0;
        if (lines[0]) {
            const header = lines[0].split(',');
            if (header.length > 9) {
                elevation = parseFloat(header[9]);
                if (!isNaN(elevation)) {
                    console.log(`Elevation from EPW file: ${elevation}m`);
                }
            }
        }

        // Calculate wet bulb temperatures using Python script
        console.log('Starting wet bulb temperature calculations...');
        try {
            const pythonPath = 'python'; // or 'python3'
            const scriptPath = path.join(__dirname, '..', '..', 'python', 'psychrolib.py');

            // Create temporary files
            const tempDir = os.tmpdir();
            const inputFile = path.join(tempDir, 'psychrolib_input.json');
            const outputFile = path.join(tempDir, 'psychrolib_output.json');

            // Prepare and write input data
            const inputData = {
                dryBulb: dbt,
                relHum: rh.map(h => h / 100), // Convert percentage to decimal
                elevation: elevation
            };
            fs.writeFileSync(inputFile, JSON.stringify(inputData));

            // Spawn Python process
            const process = spawn(pythonPath, [scriptPath, inputFile, outputFile]);

            // Wait for Python process to complete
            await new Promise((resolve, reject) => {
                process.on('close', (code) => {
                    if (code !== 0) {
                        reject(new Error('Python script failed'));
                    } else {
                        resolve();
                    }
                });

                process.stderr.on('data', (data) => {
                    console.error(`Python stderr: ${data}`);
                });
            });

            // Read and parse the result
            const result = JSON.parse(fs.readFileSync(outputFile, 'utf8'));
            wbt.push(...result.wet_bulb);

            // Clean up temporary files
            fs.unlinkSync(inputFile);
            fs.unlinkSync(outputFile);

            console.log('Completed all wet bulb temperature calculations');

        } catch (error) {
            console.error('Error calculating wet bulb temperatures:', error);
            return res.status(500).json({ error: 'Failed to calculate wet bulb temperatures' });
        }

        console.log('Calculating monthly summaries...');
        const monthLengths = [744, 672, 744, 720, 744, 720, 744, 744, 720, 744, 720, 744];
        let start = 0;
        const summary = monthLengths.map((length, i) => {
            console.log(`Processing month ${i + 1}...`);
            const end = start + length;
            const slice = arr => arr.slice(start, end);
            const avg = arr => arr.length ? Number((arr.reduce((a, b) => a + b, 0) / arr.length).toFixed(2)) : null;
            const max = arr => arr.length ? Number(Math.max(...arr).toFixed(2)) : null;
            const min = arr => arr.length ? Number(Math.min(...arr).toFixed(2)) : null;
            const avgNonZero = arr => {
                const nonZero = arr.filter(v => v !== 0);
                return nonZero.length ? Number((nonZero.reduce((a, b) => a + b, 0) / nonZero.length).toFixed(2)) : null;
            };

            const result = {
                month: i + 1,
                dbt_avg: avg(slice(dbt)),
                dbt_max: max(slice(dbt)),
                dbt_min: min(slice(dbt)),
                dpt_avg: avg(slice(dpt)),
                rh_avg: avg(slice(rh)),
                wbt_avg: avg(slice(wbt)),
                wet_bulb_depression_avg: avg(slice(dbt).map((val, idx) => val - slice(wbt)[idx])),
                ghi_avg:avg(slice(ghi)),
                dni_avg:avg(slice(dni)),
                ghr_avg: avgNonZero(slice(ghr)), 
                dnr_avg: avgNonZero(slice(dnr)), 
                dhr_avg: avgNonZero(slice(dhr)),
                ghr_max: max(slice(ghr)),
                dnr_max: max(slice(dnr)),
                dhr_max: max(slice(dhr)),
                ghi_max: max(slice(ghi)),
                dni_max: max(slice(dni)),
            };

            start = end;
            return result;
        });

        console.log('Summary calculation complete. Sending response...');
        res.json({ filename: req.params.filename, summary });
    });
};
