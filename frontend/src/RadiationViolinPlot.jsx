import React, { useEffect, useState } from 'react';
import Plotly from 'plotly.js-dist-min';

const MONTH_LABELS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const RAD_TYPES = [
  { key: 'ghr', label: 'GHR', color: '#ff9800', title: 'Global Horizontal Radiation' },
  { key: 'dnr', label: 'DNR', color: '#1976d2', title: 'Direct Normal Radiation' },
  { key: 'dhr', label: 'DR', color: '#43a047', title: 'Diffused Horizontal Radiation' },
];

export default function RadiationViolinPlot({ district = 'Ajmer' }) {
  const [data, setData] = useState(null);
  const [annualAvg, setAnnualAvg] = useState([null, null, null]);

  useEffect(() => {
    fetch(`http://localhost:3000/api/epw/radiation-monthwise/district/${encodeURIComponent(district)}`)
      .then(res => res.json())
      .then(json => {
        setData(json);
        // Calculate annual averages for GHR, DNR, DR
        const avgs = ['ghr', 'dnr', 'dhr'].map(key => {
          const flat = json[key].flat();
          return flat.length ? Number((flat.reduce((a, b) => a + b, 0) / flat.length).toFixed(2)) : '--';
        });
        setAnnualAvg(avgs);
      });
  }, [district]);

  useEffect(() => {
    if (!data) return;

    function buildPlot(visibleTypes = [true, true, true]) {
      const plotData = [];
      const xLabels = [];

      MONTH_LABELS.forEach(month => {
        RAD_TYPES.forEach(type => {
          xLabels.push(`${month} (${type.label})`);
        });
      });

      MONTH_LABELS.forEach((month, monthIdx) => {
        RAD_TYPES.forEach((radType, typeIdx) => {
          if (!visibleTypes[typeIdx]) return;
          plotData.push({
            type: 'violin',
            y: radType.key === 'ghr' ? data[radType.key][monthIdx].map(v => parseFloat(v)).filter(v => v !== 0) : data[radType.key][monthIdx].map(v => parseFloat(v)), // Filter out 0s for GHR as they might skew the plot
            x: Array(data[radType.key][monthIdx].length).fill(`${month} (${radType.label})`),
            name: radType.label,
            box: { visible: true },
            hoverinfo: 'skip',
            meanline: { visible: true },
            line: { color: radType.color },
            fillcolor: radType.color + '22',
            opacity: 0.7,
            width: 0.7,
            spanmode: 'hard',
            showlegend: monthIdx === 0,
            legendgroup: radType.label,
            points: 'outliers',
            scalemode: 'count',
            hovertemplate: `${month} (${radType.label})<br>` +
              'y: %{y:.2f}, kde: %{density:.2f}<extra></extra>'
          });
        });
      });

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

      const width = null;
      const height = 420;
      const visibleCount = visibleTypes.filter(Boolean).length;
      let title = 'Monthly Radiation Distribution';
      if (visibleCount === 1) title += ' (Single Type)';
      else if (visibleCount === 2) title += ' (Two Types)';

      Plotly.newPlot('radiation-violin-plot', plotData, {
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
          title: 'Radiation (Wh/m²)',
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
        hovermode: 'x unified',
        shapes,
        legend: { orientation: 'h', y: 1.08, x: 0.5, xanchor: 'center', font: { size: 13 } },
      },  { displayModeBar: true, responsive: true, displaylogo: false });
    }

    buildPlot([true, true, true]);

    const plotDiv = document.getElementById('radiation-violin-plot');
    if (plotDiv) {
      plotDiv.on('plotly_restyle', function() {
        const legendGroups = RAD_TYPES.map(t => t.label);
        const visibilities = legendGroups.map(lg => {
          const trace = plotDiv.data.find(tr => tr.legendgroup === lg);
          return trace && (trace.visible === undefined || trace.visible === true);
        });
        buildPlot(visibilities);
      });
    }
  }, [data]);

  return (
    <div style={{ width: '100%', overflow: 'hidden' }}>
      <div id="radiation-violin-plot" style={{ width: '100%' }}></div>
      {annualAvg[0] && (
        <div style={{ marginTop: '20px', textAlign: 'center' }}>
         
        </div>
      )}
    </div>
  );
}
