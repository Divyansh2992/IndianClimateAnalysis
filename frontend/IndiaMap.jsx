import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { feature } from 'topojson-client';

// Example color mapping for climate types
const CLIMATE_COLORS = {
  'Hot-dry': '#d32f2f',
  'Hot-humid': '#7b1fa2',
  'Composite-dry': '#ffd54f',
  'Composite-humid': '#ff9800',
  'Temperate': '#00bcd4',
  'Cold': '#1976d2',
  'default': '#b3d1ff',
};

const CLIMATE_LABELS = [
  { type: 'Hot-dry', color: '#d32f2f' },
  { type: 'Hot-humid', color: '#7b1fa2' },
  { type: 'Composite-dry', color: '#ffd54f' },
  { type: 'Composite-humid', color: '#ff9800' },
  { type: 'Temperate', color: '#00bcd4' },
  { type: 'Cold', color: '#1976d2' },
];

export default function IndiaMap({ onDistrictClick, onDistrictHover, climateData = {} }) {
  const svgRef = useRef();
  const [tooltip, setTooltip] = useState({ visible: false, x: 0, y: 0, name: '' });
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);

  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth < 768);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  // Responsive SVG size
  const aspectWidth = isMobile ? 430 : 900;
  const aspectHeight = isMobile ? 430 : 580;
  // For mobile, fill more of the screen
  const mobileHeight = Math.min(window.innerWidth * 1.1, window.innerHeight * 0.7);

  useEffect(() => {
    d3.json('/india.json').then((topology) => {
      const india = feature(topology, topology.objects.districts);
      const projection = d3.geoMercator().fitSize([aspectWidth, aspectHeight], india);
      const path = d3.geoPath().projection(projection);
      const svg = d3.select(svgRef.current);
      svg.selectAll('path')
        .data(india.features)
        .join('path')
        .attr('d', path)
        .attr('fill', d => CLIMATE_COLORS[climateData[d.properties.district]] || CLIMATE_COLORS['default'])
        .attr('stroke', '#333')
        .attr('stroke-width', 0.7)
        .on('mouseover', function (event, d) {
          d3.select(this).attr('fill', d3.color(CLIMATE_COLORS[climateData[d.properties.district]] || CLIMATE_COLORS['default']).darker(0.7));
          setTooltip({
            visible: true,
            x: event.clientX,
            y: event.clientY,
            name: d.properties.district,
          });
          if (onDistrictHover) onDistrictHover(d.properties.district);
        })
        .on('mousemove', function (event) {
          setTooltip(t => ({ ...t, x: event.clientX, y: event.clientY }));
        })
        .on('mouseout', function (event, d) {
          d3.select(this).attr('fill', CLIMATE_COLORS[climateData[d.properties.district]] || CLIMATE_COLORS['default']);
          setTooltip({ visible: false, x: 0, y: 0, name: '' });
          if (onDistrictHover) onDistrictHover(null);
        })
        .on('click', function (event, d) {
          if (onDistrictClick) onDistrictClick(d.properties.district);
        });
    });
  }, [onDistrictClick, onDistrictHover, climateData, aspectWidth, aspectHeight]);

  return (
    <div
      className="container-fluid position-relative p-0"
      style={{
        maxWidth: isMobile ? '100vw' : 1100,
        width: isMobile ? '100vw' : undefined,
        padding: 0,
        margin: 0,
      }}
    >
      <div className="row justify-content-center" style={{ margin: 0 }}>
        <div className={isMobile ? '' : 'col-12 col-md-10 mx-auto'} style={{ padding: 0 }}>
          <div
            className="w-100"
            style={{
              position: 'relative',
              width: isMobile ? '100vw' : undefined,
              height: isMobile ? mobileHeight : undefined,
              minHeight: isMobile ? mobileHeight : undefined,
              maxHeight: isMobile ? mobileHeight : undefined,
              paddingTop: isMobile ? 0 : `${(aspectHeight / aspectWidth) * 100}%`,
            }}
          >
            <svg
              ref={svgRef}
              viewBox={`0 0 ${aspectWidth} ${aspectHeight}`}
              preserveAspectRatio="xMidYMid meet"
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                width: '100%',
                height: '100%',
                display: 'block',
                background: '#f5f5f5',
                borderRadius: 8,
              }}
            />
            {/* Legend: below map on mobile, floating top-right on desktop */}
            {isMobile ? (
              <div className="card shadow-sm mt-2 mb-2 mx-auto" style={{ maxWidth: 320, fontSize: 15, borderRadius: 8, padding: 12 }}>
                <div className="fw-bold mb-2">Climate Type Legend</div>
                {CLIMATE_LABELS.map(({ type, color }) => (
                  <div key={type} className="d-flex align-items-center mb-1">
                    <span style={{ width: 18, height: 18, background: color, display: 'inline-block', borderRadius: 3, marginRight: 8, border: '1px solid #ccc' }}></span>
                    <span>{type}</span>
                  </div>
                ))}
              </div>
            ) : (
              <div
                className="card shadow-sm position-absolute"
                style={{
                  top: 16,
                  right: 16,
                  minWidth: 180,
                  zIndex: 10,
                  background: '#fff',
                  borderRadius: 8,
                  padding: 12,
                  fontSize: 15,
                }}
              >
                <div className="fw-bold mb-2">Climate Type Legend</div>
                {CLIMATE_LABELS.map(({ type, color }) => (
                  <div key={type} className="d-flex align-items-center mb-1">
                    <span style={{ width: 18, height: 18, background: color, display: 'inline-block', borderRadius: 3, marginRight: 8, border: '1px solid #ccc' }}></span>
                    <span>{type}</span>
                  </div>
                ))}
              </div>
            )}
            {/* Tooltip */}
            {tooltip.visible && (
              <div
                className="position-fixed bg-dark text-white px-2 py-1 rounded shadow-sm"
                style={{
                  left: tooltip.x + 12,
                  top: tooltip.y + 12,
                  pointerEvents: 'none',
                  fontSize: 14,
                  zIndex: 9999,
                  whiteSpace: 'nowrap',
                }}
              >
                {tooltip.name}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
