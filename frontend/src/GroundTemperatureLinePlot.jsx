import React, { useEffect, useState } from 'react';
import Plotly from 'plotly.js-dist-min';

const MONTH_LABELS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const COLORS = ['#7ecbff', '#ffb97e', '#7effa1'];

export default function GroundTemperatureLinePlot({ district = 'Ajmer' }) {
  const [data, setData] = useState(null);
  const [location, setLocation] = useState(null);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/api/epw/ground-temp/district/${encodeURIComponent(district)}`)
      .then(res => res.json())
      .then(json => {
        setData(json.monthlyData);
        setLocation(json.location);
      });
  }, [district]);

  useEffect(() => {
    if (!data) return;
    const trace0 = {
      x: MONTH_LABELS,
      y: data.map(m => m.header_0_5m),
      mode: 'lines+markers',
      name: '0.5 meters',
      line: { color: COLORS[0], width: 3 },
      marker: { color: COLORS[0], size: 8 }
    };
    const trace1 = {
      x: MONTH_LABELS,
      y: data.map(m => m.header_2m),
      mode: 'lines+markers',
      name: '2.0 meters',
      line: { color: COLORS[1], width: 3 },
      marker: { color: COLORS[1], size: 8 }
    };
    const trace2 = {
      x: MONTH_LABELS,
      y: data.map(m => m.header_4m),
      mode: 'lines+markers',
      name: '4.0 meters',
      line: { color: COLORS[2], width: 3 },
      marker: { color: COLORS[2], size: 8 }
    };

    Plotly.newPlot('ground-temp-line-plot', [trace0, trace1, trace2], {
      title: '',
      xaxis: {
        title: 'Month',
        tickvals: MONTH_LABELS,
        ticktext: MONTH_LABELS,
        showgrid: false,
        zeroline: false,
        showline: true,
        linecolor: '#888',
        tickfont: { size: 12 }
      },
      yaxis: {
        title: 'Temperature °C',
        zeroline: false,
        gridcolor: '#e0e0e0',
        tickfont: { size: 12 }
      },
      margin: { l: 60, r: 20, t: 60, b: 30 },
      plot_bgcolor: '#fff',
      paper_bgcolor: '#fff',
      font: { family: 'system-ui', size: 13, color: '#222' },
      width: 900,
      height: 400,
      violinmode: 'group',
      showlegend: true,
      legend: { orientation: 'h', y: 1.08, x: 0.5, xanchor: 'center', font: { size: 13 } },
      hovermode: 'x unified',
    },  { displayModeBar: true, responsive: true, displaylogo: false, modeBarButtonsToRemove: ['select2d', 'lasso2d'] });
  }, [data]);

  return (
    <div className="container-fluid px-3 py-3" style={{background:'#fff', borderRadius:8, marginTop:4}}>
      <div className="row align-items-start g-0">
        <div className="col" style={{minWidth:180, marginLeft:24, marginRight:24}}>
          <div className="fw-bold" style={{ fontSize: 22, marginBottom: 16 }}>LEGEND</div>
          <div className="fw-semibold mb-2">DEPTH</div>
          <div className="d-flex flex-column gap-2">
            <div className="d-flex align-items-center mb-2">
              <div style={{ width: 18, height: 18, background: COLORS[0], borderRadius: 4, marginRight: 10 }} />
              <span style={{ fontSize: 16 }}>0.5 meters</span>
            </div>
            <div className="d-flex align-items-center mb-2">
              <div style={{ width: 18, height: 18, background: COLORS[1], borderRadius: 4, marginRight: 10 }} />
              <span style={{ fontSize: 16 }}>2.0 meters</span>
            </div>
            <div className="d-flex align-items-center mb-2">
              <div style={{ width: 18, height: 18, background: COLORS[2], borderRadius: 4, marginRight: 10 }} />
              <span style={{ fontSize: 16 }}>4.0 meters</span>
            </div>
          </div>
          {location && (
            <div className="mt-4" style={{ fontSize: 15 }}>
              <div><b>Location:</b> {location.city}, {location.country}</div>
              <div><b>Latitude/Longitude:</b> {location.latitude} / {location.longitude}</div>
              <div><b>Elevation / Time zone:</b> {location.elevation} / {location.timezone}</div>
            </div>
          )}
        </div>
        <div className="col ps-0 mb-2">
          <div id="ground-temp-line-plot" className="w-100" style={{ minHeight: 400, marginTop: 0 }} />
        </div>
      </div>
    </div>
  );
}