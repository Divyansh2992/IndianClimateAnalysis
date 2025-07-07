import React, { useEffect, useState } from 'react';
import Plotly from 'plotly.js-dist-min';

const MONTH_LABELS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const HOUR_LABELS = [
  '0 a.m.', '1 a.m.', '2 a.m.', '3 a.m.', '4 a.m.', '5 a.m.', '6 a.m.', '7 a.m.', '8 a.m.', '9 a.m.', '10 a.m.', '11 a.m.',
  '12 p.m.', '1 p.m.', '2 p.m.', '3 p.m.', '4 p.m.', '5 p.m.', '6 p.m.', '7 p.m.', '8 p.m.', '9 p.m.', '10 p.m.', '11 p.m.'
];

const COLORMAP_CONFIGS = {
  dbt: {
    title: 'Dry Bulb Temperature (°C)',
    unit: '°C',
    zmin: 5,
    zmax: 40,
    colorscale: [
      [0, '#0033a0'],    // < 15°C deep blue
      [0.25, '#7ecbff'], // 15-25°C light blue
      [0.5, '#fff'],     // 25°C white
      [0.75, '#ffb3b3'], // 25-35°C lighter red
      [1, '#ff6666']     // > 35°C lighter red
    ],
    legendRanges: [
      { color: '#0033a0', label: '< 15°C' },
      { color: '#7ecbff', label: '> 15°C and < 25°C' },
      { color: '#ffb3b3', label: '> 25°C and < 35°C' },
      { color: '#ff6666', label: '> 35°C' }
    ]
  },
  wbt: {
    title: 'Wet Bulb Temperature (°C)',
    unit: '°C',
    zmin: 0,
    zmax: 35,
    colorscale: [
      [0, '#0033a0'],    // < 15°C deep blue
      [0.25, '#7ecbff'], // 15-25°C light blue
      [0.5, '#fff'],     // 25°C white
      [0.75, '#ffb3b3'], // 25-35°C lighter red
      [1, '#ff6666']     // > 35°C lighter red
    ],
    legendRanges: [
      { color: '#0033a0', label: '< 15°C' },
      { color: '#7ecbff', label: '> 15°C and < 25°C' },
      { color: '#ffb3b3', label: '> 25°C and < 35°C' },
      { color: '#ff6666', label: '> 35°C' }
    ]
  },
  dpt: {
    title: 'Dew Point Temperature (°C)',
    unit: '°C',
    zmin: -10,
    zmax: 30,
    colorscale: [
      [0, '#0033a0'],    // < 15°C deep blue
      [0.25, '#7ecbff'], // 15-25°C light blue
      [0.5, '#fff'],     // 25°C white
      [0.75, '#ffb3b3'], // 25-35°C lighter red
      [1, '#ff6666']     // > 35°C lighter red
    ],
    legendRanges: [
      { color: '#0033a0', label: '< 15°C' },
      { color: '#7ecbff', label: '> 15°C and < 25°C' },
      { color: '#ffb3b3', label: '> 25°C and < 35°C' },
      { color: '#ff6666', label: '> 35°C' }
    ]
  },
  rh: {
    title: 'Relative Humidity (%)',
    unit: '%',
    zmin: 0,
    zmax: 100,
    colorscale: [
      [0, '#0033a0'],    // < 15°C deep blue
      [0.25, '#7ecbff'], // 15-25°C light blue
      [0.5, '#fff'],     // 25°C white
      [0.75, '#ffb3b3'], // 25-35°C lighter red
      [1, '#ff6666']     // > 35°C lighter red
    ],
    legendRanges: [
      { color: '#0033a0', label: '< 15°C' },
      { color: '#7ecbff', label: '> 15°C and < 25°C' },
      { color: '#ffb3b3', label: '> 25°C and < 35°C' },
      { color: '#ff6666', label: '> 35°C' }
    ]
  }
};

// Map for full forms of radio button options
const RADIO_FULL_FORMS = {
  dbt: 'Dry Bulb Temperature',
  wbt: 'Wet Bulb Temperature',
  dpt: 'Dew Point Temperature',
  rh: 'Relative Humidity',
};

export default function HourlyColormapPlot({ district = 'Jaipur-Sanganer' }) {
  const [data, setData] = useState(null);
  const [selectedType, setSelectedType] = useState('dbt'); // New state for selected colormap type

  useEffect(() => {
    fetch(`http://localhost:3000/api/epw/hourly-colormap/district/${encodeURIComponent(district)}`)
      .then(res => res.json())
      .then(json => setData(json)); // Store the entire JSON response (dbt_array, wbt_array, etc.)
  }, [district]);

  useEffect(() => {
    if (!data) return;

    const config = COLORMAP_CONFIGS[selectedType]; // Get config based on selected type

    // X axis: 365 days, but we want to show months as minor ticks
    const xTicks = [];
    const xTickLabels = [];
    for (let i = 0; i < 12; i++) {
      xTicks.push(i * 30.4166 + 15.5); // Middle of each month
      xTickLabels.push(MONTH_LABELS[i]);
    }

    Plotly.newPlot('hourly-colormap-plot', [{
      z: data[`${selectedType}_array`], // Use selected data array
      type: 'heatmap',
      colorscale: config.colorscale,
      zmin: config.zmin,
      zmax: config.zmax,
      colorbar: {
        title: config.unit,
        tickvals: config.legendRanges.map((_, i) => config.zmin + (config.zmax - config.zmin) / (config.legendRanges.length) * i),
        ticktext: config.legendRanges.map(range => range.label),
        len: 0.8,
        thickness: 18,
        y: 0.5,
        yanchor: 'middle'
      }
    }], {
      title: config.title, // Use dynamic title
      xaxis: {
        title: '',
        showgrid: false,
        zeroline: false,
        showline: true,
        linecolor: '#888',
        tickvals: xTicks,
        ticktext: xTickLabels,
        ticks: '',
        tickfont: { size: 12 }
      },
      yaxis: {
        title: 'Hour',
        showgrid: false,
        zeroline: false,
        showline: true,
        linecolor: '#888',
        tickvals: [0,2,4,6,8,10,12,14,16,18,20,22],
        ticktext: [
          '0 a.m.','2 a.m.','4 a.m.','6 a.m.','8 a.m.','10 a.m.',
          '12 p.m.','2 p.m.','4 p.m.','6 p.m.','8 p.m.','10 p.m.'
        ],
        autorange: false,
        range: [-0.5, 23.5],
        tickfont: { size: 12 }
      },
      margin: { l: 60, r: 20, t: 60, b: 30 },
      plot_bgcolor: '#fff',
      paper_bgcolor: '#fff',
      font: { family: 'system-ui', size: 13, color: '#222' },
      width: 900,
      height: 400,
      hovermode: false,
      showlegend: false
    },  { displayModeBar: true, responsive: true, displaylogo: false });
  }, [data, selectedType]); // Re-render when data or selectedType changes

  return (
    <div className="container-fluid px-3 py-3" style={{ background: '#fff', borderRadius: 8, marginTop: 4, marginBottom: 4, paddingBottom: 4 }}>
      <div className="row align-items-start g-0">
        {/* Left legend panel */}
        <div className="col-12 col-md-auto mb-3 mb-md-0 ms-md-3 me-md-4" style={{ minWidth: 180 }}>
          <div className="border rounded-3 p-3 bg-light d-flex flex-column align-items-center h-100" style={{ borderColor: '#e0e0e0' }}>
            <div className="fw-bold" style={{ fontSize: 22, marginBottom: 16, letterSpacing: 1 }}>LEGEND</div>
            <div className="fw-semibold mb-2" style={{ fontSize: 17 }}>Temperature Range</div>
            <div className="d-flex flex-column gap-2 mb-3 w-100">
              {COLORMAP_CONFIGS[selectedType].legendRanges.map((range, idx) => (
                <div key={idx} className="d-flex align-items-center w-100" style={{ whiteSpace: 'nowrap' }}>
                  <div style={{ width: 48, height: 24, background: range.color, marginRight: 10, borderRadius: 4, display: 'inline-block' }} />
                  <span style={{ fontSize: 16, display: 'inline-block', verticalAlign: 'middle' }}>{range.label}</span>
                </div>
              ))}
            </div>
            <div className="d-flex flex-column gap-2 mt-3 w-100 align-items-start">
              {Object.keys(COLORMAP_CONFIGS).map(key => (
                <div key={key} className="d-flex align-items-center w-100">
                  <input
                    type="radio"
                    id={key}
                    name="colormapType"
                    value={key}
                    checked={selectedType === key}
                    onChange={() => setSelectedType(key)}
                    className="form-check-input"
                  />
                  <label htmlFor={key} className={selectedType === key ? 'ms-2 fw-bold' : 'ms-2'} style={{ fontSize: 15 }}>
                    {RADIO_FULL_FORMS[key]}
                  </label>
                </div>
              ))}
            </div>
          </div>
        </div>
        {/* Plot area */}
        <div className="col-12 col-md ps-0">
          <div id="hourly-colormap-plot" className="w-100" style={{ minHeight: 400, marginTop: 0 }} />
        </div>
      </div>
    </div>
  );
}