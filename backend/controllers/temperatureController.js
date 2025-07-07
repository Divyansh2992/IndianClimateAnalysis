const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const os = require('os');

// GET /api/epw/temperature-monthwise/:filename - Return monthwise temperature arrays for plotting
exports.getTemperatureMonthwise = async (req, res) => {
    console.log('Starting temperature calculations...');
    const filePath = req.epwFilePath;
    
    fs.readFile(filePath, 'utf8', async (err, data) => {
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

        const dataLines = lines.slice(8);
        const dbt = [], dpt = [], wbt = [], rh = [];

        console.log('Extracting hourly data...');
        for (const line of dataLines) {
            const cols = line.split(',');
            if (cols.length < 22) continue;
            dbt.push(parseFloat(cols[6]));   // Dry bulb temperature (°C)
            dpt.push(parseFloat(cols[7]));   // Dew point temperature (°C)
            rh.push(parseFloat(cols[8]));    // Relative humidity (%)
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

        // Month slicing
        console.log('Processing monthly data...');
        const monthLengths = [744, 672, 744, 720, 744, 720, 744, 744, 720, 744, 720, 744];
        let start = 0;
        const dbtMonth = [], wbtMonth = [], dptMonth = [];
        for (let m = 0; m < 12; m++) {
            console.log(`Processing month ${m + 1}...`);
            const end = start + monthLengths[m];
            dbtMonth.push(dbt.slice(start, end));
            wbtMonth.push(wbt.slice(start, end));
            dptMonth.push(dpt.slice(start, end));
            start = end;
        }

        console.log('Temperature calculations complete. Sending response...');
        res.json({ dbt: dbtMonth, wbt: wbtMonth, dpt: dptMonth });
    });
};
