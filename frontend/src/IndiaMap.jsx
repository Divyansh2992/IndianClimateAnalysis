import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { feature, mesh } from 'topojson-client';

// Define a color for each climate type
const CLIMATE_COLORS = {
  'Hot_dry': '#FF0000',      // strong red
  'Hot_humid': '#800000',   // rich brown
  'Composite_1': '#FFDB58', // soft yellow
  'Composite_2': '#ffa700', // orange
  'Temperate': '#00FFFF',   // blue
  'Cold': '#0A3CCF',        // deep blue
  '': 'pink',            // fallback: light gray
};

const LEGEND_LABELS = {
  'Hot_dry': 'Hot-dry',
  'Hot_humid': 'Hot-humid',
  'Composite_1': 'Composite-dry',
  'Composite_2': 'Composite-humid',
  'Temperate': 'Temperate',
  'Cold': 'Cold',
};

export default function IndiaMap({ onDistrictClick, onDistrictHover }) {
  const svgRef = useRef();
  const [climateTypes, setClimateTypes] = useState({});

  useEffect(() => {
    // Fetch climate type mapping
    fetch(`${import.meta.env.VITE_API_URL}/api/epw/climate-types`)
      .then(res => res.json())
      .then(setClimateTypes)
      .catch(() => setClimateTypes({}));
  }, []);

  useEffect(() => {
    d3.json(`${import.meta.env.VITE_API_URL}/india.json`).then((topology) => {
      const india = feature(topology, topology.objects.districts);
      const width = 900;
      const height = 580;
      const projection = d3.geoMercator().fitSize([width, height], india);
      const path = d3.geoPath().projection(projection);
      const svg = d3.select(svgRef.current)
        .attr('width', width)
        .attr('height', height);
      // Draw districts
      svg.selectAll('path.district')
        .data(india.features)
        .join('path')
        .attr('class', 'district')
        .attr('d', path)
        .attr('fill', d => {
          const district = (d.properties.district || '').trim().toLowerCase();
          const state = (d.properties.st_nm || '').trim().toLowerCase();
          const key = `${district}|${state}`;
          const climate = climateTypes[key] || '';
          return CLIMATE_COLORS[climate] || '#e0e0e0';
        })
        .attr('stroke', '#fff')
        .attr('stroke-width', 0.5)
        .on('mouseover', function (event, d) {
          d3.select(this).attr('fill', '#ffcc00');
          const [x, y] = d3.pointer(event, svg.node());
          d3.select('#tooltip')
            .style('left', `${x + 20}px`)
            .style('top', `${y + 20}px`)
            .style('display', 'block')
            .text(d.properties.district);
          if (onDistrictHover) onDistrictHover(d.properties.district, d.properties.st_nm);
        })
        .on('mousemove', function (event) {
          const [x, y] = d3.pointer(event, svg.node());
          d3.select('#tooltip')
            .style('left', `${x + 20}px`)
            .style('top', `${y + 20}px`);
        })
        .on('mouseout', function (event, d) {
          // Restore color based on climate type
          const district = (d.properties.district || '').trim();
          const state = (d.properties.st_nm || '').trim();
          const key = `${district}|${state}`;
          const climate = climateTypes[key] || '';
          d3.select(this).attr('fill', CLIMATE_COLORS[climate] || '#b3d1ff');
          d3.select('#tooltip').style('display', 'none');
          if (onDistrictHover) onDistrictHover(null, null);
        })
        .on('click', function (event, d) {
          if (onDistrictClick) onDistrictClick(d.properties.district, d.properties.st_nm);
        });

      // Draw state boundaries if available
      if (topology.objects.states) {
        const stateMesh = mesh(topology, topology.objects.states, (a, b) => a !== b);
        svg.append('path')
          .datum(stateMesh)
          .attr('d', path)
          .attr('fill', 'none')
          .attr('stroke', '#000')
          .attr('stroke-width', 2)
          .attr('stroke-opacity', 0.3)
          .attr('pointer-events', 'none');
      }

      // Draw country boundary (outer outline)
      if (topology.objects.districts) {
        const countryMesh = mesh(topology, topology.objects.districts, (a, b) => a === b);
        svg.append('path')
          .datum(countryMesh)
          .attr('d', path)
          .attr('fill', 'none')
          .attr('stroke', '#000')
          .attr('stroke-width', 2)
          .attr('stroke-opacity', 0.4)
          .attr('pointer-events', 'none');
      }
    });
  }, [onDistrictClick, onDistrictHover, climateTypes]);

  return (
    <>
      <svg ref={svgRef}></svg>
      <div style={{
        position: 'absolute',
        top: 35,
        right: 470,
        background: '#fff',
        border: '1px solid #ddd',
        borderRadius: 5,
        padding: '6px 10px',
        boxShadow: '0 1px 4px rgba(0,0,0,0.04)',
        display: 'inline-block',
        fontSize: 13,
        zIndex: 10,
      }}>
        <b style={{ fontSize: 14, marginBottom: 6, display: 'block' }}>Climate Type Legend</b>
        {Object.entries(LEGEND_LABELS).map(([key, label]) => (
          <div key={key} style={{ display: 'flex', alignItems: 'center', marginBottom: 4 }}>
            <span style={{
              display: 'inline-block',
              width: 16,
              height: 16,
              background: CLIMATE_COLORS[key],
              border: '1px solid #bbb',
              borderRadius: 3,
              marginRight: 7,
            }}></span>
            <span>{label}</span>
          </div>
        ))}
      </div>
    </>
  );
}
