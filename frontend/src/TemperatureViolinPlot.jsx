import React, { useEffect, useState } from 'react';
import Plotly from 'plotly.js-dist-min';

const MONTH_LABELS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const TEMP_TYPES = [
  { key: 'dbt', label: 'DBT', color: '#1976d2', title: 'Dry Bulb Temperature' },
  { key: 'wbt', label: 'WBT', color: '#00bcd4', title: 'Wet Bulb Temperature' },
  { key: 'dpt', label: 'DPT', color: '#8bc34a', title: 'Dew Point Temperature' }
];

export default function TemperatureViolinPlot({ district = 'Ajmer' }) {
  const [data, setData] = useState(null);
  const [design, setDesign] = useState([null, null, null]);

  useEffect(() => {
    fetch(`http://localhost:3000/api/epw/temperature-monthwise/district/${encodeURIComponent(district)}`)
      .then(res => res.json())
      .then(json => {
        setData(json);
        // Calculate design conditions for DBT, WBT, DPT
        const designConds = ['dbt', 'wbt', 'dpt'].map(key => {
          const flat = json[key].flat().sort((a, b) => b - a);
          return [flat[35], flat[87], flat[175]];
        });
        setDesign(designConds);
      });
  }, [district]);

  useEffect(() => {
    if (!data) return;

    // Helper to build plot and layout
    function buildPlot(visibleTypes = [true, true, true]) {
      const plotData = [];
      const xLabels = [];
      // Restore original xLabels: Jan (DPT), Jan (WBT), Jan (DBT), Feb (DPT), ...
      MONTH_LABELS.forEach(month => {
        TEMP_TYPES.forEach(type => {
          xLabels.push(`${month} (${type.label})`);
        });
      });
      // Create data for each month and temperature type
      MONTH_LABELS.forEach((month, monthIdx) => {
        TEMP_TYPES.forEach((tempType, typeIdx) => {
          if (!visibleTypes[typeIdx]) return;
          plotData.push({
            type: 'violin',
            y: data[tempType.key][monthIdx].map(v => parseFloat(v)),
            x: Array(data[tempType.key][monthIdx].length).fill(`${month} (${tempType.label})`),
            name: tempType.label,
            box: { visible: true },
            meanline: { visible: true },
            line: { color: tempType.color },
            fillcolor: tempType.color + '22',
            opacity: 0.7,
            width: 0.7,
            spanmode: 'hard',
            showlegend: monthIdx === 0,
            legendgroup: tempType.label,
            points: 'outliers',
            scalemode: 'count',
            hovertemplate: `${month} (${tempType.label})<br>` +
              'y: %{y:.2f}, kde: %{density:.2f}<extra></extra>'
          });
        });
      });
      // Create shapes for month separators (more transparent)
      const shapes = [];
      for (let i = 3; i < xLabels.length; i += 3) {
        shapes.push({
          type: 'line',
          x0: i - 0.5,
          x1: i - 0.5,
          y0: 0,
          y1: 1,
          yref: 'paper',
          line: {
            color: 'rgba(128, 128, 128, 0.08)',
            width: 2,
            dash: 'solid'
          }
        });
      }
      // Responsive width and reduced height
      const width = null; // Let Plotly use the container's width
      const height = 420;
      // Dynamic title
      const visibleCount = visibleTypes.filter(Boolean).length;
      let title = 'Monthly Temperature Distribution';
      if (visibleCount === 1) title += ' (Single Type)';
      else if (visibleCount === 2) title += ' (Two Types)';
      Plotly.newPlot('violin-plot', plotData, {
        title,
        xaxis: {
          title: 'Month',
          tickvals: MONTH_LABELS.map((_, i) => i * 3 + 1),
          ticktext: MONTH_LABELS,
          showgrid: false,
          zeroline: false,
          showline: true,
          linecolor: '#888',
          tickfont: { size: 11 },
          tickangle: 0
        },
        yaxis: {
          title: 'Temperature °C',
          zeroline: false,
          gridcolor: '#e0e0e0',
          tickfont: { size: 13 }
        },
        margin: { l: 60, r: 20, t: 60, b: 30 },
        plot_bgcolor: '#fff',
        paper_bgcolor: '#fff',
        font: { family: 'system-ui', size: 14, color: '#222' },
        width,
        height,
        violingap: 0.1,
        violingroupgap: 0.2,
        violinmode: 'group',
        showlegend: true,
        legend: { orientation: 'h', y: 1.08, x: 0.5, xanchor: 'center', font: { size: 13 } },
        hovermode: 'x unified',
        shapes
      }, { displayModeBar: true, responsive: true, displaylogo: false });
    }

    // Initial plot (all visible)
    buildPlot([true, true, true]);

    // Add event listener to update layout and data on legend click (trace hide/show)
    const plotDiv = document.getElementById('violin-plot');
    if (plotDiv) {
      plotDiv.on('plotly_restyle', function() {
        // Get current visible traces (by legendgroup)
        const legendGroups = TEMP_TYPES.map(t => t.label);
        const visibilities = legendGroups.map(lg => {
          // Find the first trace with this legendgroup
          const trace = plotDiv.data.find(tr => tr.legendgroup === lg);
          return trace && (trace.visible === undefined || trace.visible === true);
        });
        buildPlot(visibilities);
      });
    }
  }, [data]);

  return (
    <div className="container-fluid px-3 py-3">
      <div id="violin-plot" className="w-100" style={{ minHeight: 420 }}></div>
      {design[0] && (
        <div className="mt-4 text-center">
          {/* Reserved for future design condition display if needed */}
        </div>
      )}
    </div>
  );
}
