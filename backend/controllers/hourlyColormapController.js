const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process'); // Added for spawning Python process
const os = require('os'); // Added for temporary file paths
const axios = require('axios');

exports.getHourlyColormap = async (req, res) => {
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

  // Extract raw data arrays for DBT, DPT, RH
  const dbt = [], dpt = [], rh = [];
  for (const line of dataLines) {
    const cols = line.split(',');
    if (cols.length < 22) continue;
    dbt.push(parseFloat(cols[6]));   // Dry bulb temperature (°C)
    dpt.push(parseFloat(cols[7]));   // Dew point temperature (°C)
    rh.push(parseFloat(cols[8]));    // Relative humidity (%)
  }

  // Get elevation from header (needed for psychrolib.py)
  let elevation = 0;
  if (lines[0]) {
    const header = lines[0].split(',');
    if (header.length > 9) {
      elevation = parseFloat(header[9]);
    }
  }

  // Calculate wet bulb temperatures using Python script (similar to temperatureController.js)
  const wbt = [];
  try {
    const pythonPath = 'python'; // or 'python3'
    const scriptPath = path.join(__dirname, '..', '..', 'python', 'psychrolib.py');

    const tempDir = os.tmpdir();
    const inputFile = path.join(tempDir, 'psychrolib_input.json');
    const outputFile = path.join(tempDir, 'psychrolib_output.json');

    const inputData = {
      dryBulb: dbt,
      relHum: rh.map(h => h / 100), // Convert percentage to decimal
      elevation: elevation
    };
    fs.writeFileSync(inputFile, JSON.stringify(inputData));

    const process = spawn(pythonPath, [scriptPath, inputFile, outputFile]);

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

    const result = JSON.parse(fs.readFileSync(outputFile, 'utf8'));
    wbt.push(...result.wet_bulb);

    fs.unlinkSync(inputFile);
    fs.unlinkSync(outputFile);

  } catch (error) {
    console.error('Error calculating wet bulb temperatures:', error);
    return res.status(500).json({ error: 'Failed to calculate wet bulb temperatures' });
  }

  // Build 24x365 arrays for all types
  const dbt_array = Array(24).fill(null).map(() => []);
  const wbt_array = Array(24).fill(null).map(() => []);
  const dpt_array = Array(24).fill(null).map(() => []);
  const rh_array = Array(24).fill(null).map(() => []);

  for (let hour = 0; hour < 24; hour++) {
    let currentIdx = hour;
    for (let day = 0; day < 365; day++) {
      dbt_array[hour].push(dbt[currentIdx]);
      wbt_array[hour].push(wbt[currentIdx]);
      dpt_array[hour].push(dpt[currentIdx]);
      rh_array[hour].push(rh[currentIdx]);
      currentIdx += 24;
    }
  }

  res.json({ dbt_array, wbt_array, dpt_array, rh_array });
};
