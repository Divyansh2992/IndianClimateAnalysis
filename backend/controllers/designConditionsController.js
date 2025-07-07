const XLSX = require('xlsx');
const path = require('path');

const getDesignConditions = (req, res) => {
    try {
        // Accept district and state from req.params
        const { district, state } = req.params;
        if (!district || !state) {
            return res.status(400).json({
                error: 'Missing parameters',
                message: 'Both district and state are required.'
            });
        }

        // Read the Excel file
        const workbook = XLSX.readFile(path.join(__dirname, '../design_conditions(3).xlsx'));
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        // Auto-detect header row
        const data = XLSX.utils.sheet_to_json(worksheet);
        // Debug: print the first row's keys
        if (data.length > 0) {
        }

        // Find the row matching both District_json and State_json
        const match = data.find(row => {
            const districtJson = (row.District_json || '').trim().toLowerCase();
            const stateJson = (row.State_json || '').trim().toLowerCase();
            return (
                districtJson === district.trim().toLowerCase() &&
                stateJson === state.trim().toLowerCase()
            );
        });

        if (!match) {
            // Debug: print all available district/state names for troubleshooting
            const available = data.map(row => ({
                district_json: (row.District_json || '').trim().toLowerCase(),
                state_json: (row.State_json || '').trim().toLowerCase()
            }));
            console.log('DEBUG: No match for', district, state);
            console.log('DEBUG: Available district/state names:', available);
            return res.status(404).json({
                error: 'Not found',
                message: `No design conditions found for district: ${district}, state: ${state}`
            });
        }

        // Debug: print all keys and values of the matched row
        console.log('Matched row keys:', Object.keys(match));
        console.log('Matched row:', match);

        // Robustly find the Source column (case-insensitive, trimmed)
        let source = null;
        for (const key of Object.keys(match)) {
            if (key && key.trim().toLowerCase() === 'source') {
                source = match[key];
                break;
            }
        }
        if (!source && match.__EMPTY_3) {
            source = match.__EMPTY_3;
        }

        // Use the actual keys from the Excel file as seen in the debug output
        const responseData = {
            district_json: (match.District_json || '').trim(),
            state_json: (match.State_json || '').trim(),
            source: match.Source,
            designConditions: {
                Heating: {
                    "99.60%": {
                        dryBulb: match['Heating'],
                        wetBulb: match['__EMPTY']
                    },
                    "99.00%": {
                        dryBulb: match['__EMPTY_1'],
                        wetBulb: match['__EMPTY_2']
                    }
                },
                Cooling: {
                    "Peak": {
                        dryBulb: match['Cooling'],
                        wetBulb: match['__EMPTY_3']
                    },
                    "0.40%": {
                        dryBulb: match['__EMPTY_4'],
                        wetBulb: match['__EMPTY_5']
                    },
                    "1.00%": {
                        dryBulb: match['__EMPTY_6'],
                        wetBulb: match['__EMPTY_7']
                    },
                    "2.00%": {
                        dryBulb: match['__EMPTY_8'],
                        wetBulb: match['__EMPTY_9']
                    }
                },
                Evaporation: {
                    "Peak": {
                        wetBulb: match['Evaporation'],
                        meanCoincidentDryBulb: match['__EMPTY_10']
                    },
                    "0.40%": {
                        wetBulb: match['__EMPTY_11'],
                        meanCoincidentDryBulb: match['__EMPTY_12']
                    },
                    "1.00%": {
                        wetBulb: match['__EMPTY_13'],
                        meanCoincidentDryBulb: match['__EMPTY_14']
                    },
                    "2.00%": {
                        wetBulb: match['__EMPTY_15'],
                        meanCoincidentDryBulb: match['__EMPTY_16']
                    }
                }
            },
            degreeDays: {
                CDD: match['Degree Days'] || null,
                HDD: match['__EMPTY_17'] || null
            }
        };

        res.json(responseData);
    } catch (error) {
        console.error('Error reading design conditions:', error);
        res.status(500).json({
            error: 'Internal server error',
            message: 'Failed to read design conditions data'
        });
    }
};

// New endpoint: get all climate types by city/district
const getClimateTypes = (req, res) => {
    try {
        const workbook = XLSX.readFile(path.join(__dirname, '../design_conditions(3).xlsx'));
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const data = XLSX.utils.sheet_to_json(worksheet);
        const mapping = {};
        data.forEach(row => {
            const district = (row.District_json || '').trim().toLowerCase();
            const state = (row.State_json || '').trim().toLowerCase();
            const climate = (row.Climate_type || '').trim();
            if (district && state && climate) {
                mapping[`${district}|${state}`] = climate;
            }
        });
        res.json(mapping);
    } catch (error) {
        console.error('Error reading climate types:', error);
        res.status(500).json({ error: 'Internal server error', message: 'Failed to read climate types' });
    }
};

module.exports = {
    getDesignConditions,
    getClimateTypes
}; 