const fs = require('fs');
const path = require('path');

// GET /api/epw/ground-temp/:filename - Return ground temperature data
exports.getGroundTempData = async (req, res) => {
    console.log('Starting ground temperature data extraction...');
    console.log('Reading EPW file:', req.epwFilePath);

    fs.readFile(req.epwFilePath, 'utf8', (err, data) => {
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

        // Extract location data from header
        const header = lines[0].split(',');
        const locationData = {
            city: header[1],
            state: header[2],
            country: header[3],
            latitude: parseFloat(header[6]),
            longitude: parseFloat(header[7]),
            timezone: parseFloat(header[8]),
            elevation: parseFloat(header[9])
        };

        // Extract ground temperature data from header
        const groundTempLine = lines[3]; // Ground temperature data is on line 4 (0-based index)
        if (!groundTempLine || !groundTempLine.startsWith('GROUND TEMPERATURES')) {
            console.error('Ground temperature data not found in EPW file');
            return res.status(400).json({ error: 'Ground temperature data not found' });
        }

        const groundTempData = groundTempLine.split(',');
        
        // Extract ground temperatures for each depth from header
        const grd_0_header = groundTempData.slice(6, 18).map(val => parseFloat(val));  // 0.5m depth
        const grd_1_header = groundTempData.slice(22, 34).map(val => parseFloat(val)); // 2m depth
        const grd_2_header = groundTempData.slice(38, 50).map(val => parseFloat(val)); // 4m depth

        // Process hourly data for monthly averages
        console.log('Processing hourly data for monthly averages...');
        const dataLines = lines.slice(8);
        const monthlyData = Array(12).fill().map(() => ({
            grd_0: [],
            grd_1: [],
            grd_2: []
        }));

        // Extract hourly ground temperatures
        for (const line of dataLines) {
            const cols = line.split(',');
            if (cols.length < 22) continue;

            const month = parseInt(cols[1]) - 1; // Convert to 0-based month index
            if (month >= 0 && month < 12) {
                monthlyData[month].grd_0.push(parseFloat(cols[18])); // Ground temperature at 0.5m
                monthlyData[month].grd_1.push(parseFloat(cols[19])); // Ground temperature at 2m
                monthlyData[month].grd_2.push(parseFloat(cols[20])); // Ground temperature at 4m
            }
        }

        // Calculate monthly averages
        const calculateAverage = arr => {
            const validValues = arr.filter(val => !isNaN(val));
            return validValues.length ? 
                Number((validValues.reduce((a, b) => a + b, 0) / validValues.length).toFixed(2)) : 
                null;
        };

        const monthlyAverages = monthlyData.map((monthData, index) => ({
            month: index + 1,
            monthName: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][index],
            depth_0_5m: calculateAverage(monthData.grd_0),
            depth_2m: calculateAverage(monthData.grd_1),
            depth_4m: calculateAverage(monthData.grd_2),
            header_0_5m: grd_0_header[index],
            header_2m: grd_1_header[index],
            header_4m: grd_2_header[index]
        }));

        // Prepare response data
        const response = {
            filename: req.params.filename,
            location: locationData,
            monthlyData: monthlyAverages,
            months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        };

        console.log('Ground temperature data extraction complete. Sending response...');
        res.json(response);
    });
}; 