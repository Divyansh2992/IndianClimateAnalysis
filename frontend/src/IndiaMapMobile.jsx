import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { feature, mesh } from 'topojson-client';

const CLIMATE_COLORS = {
  'Hot_dry': '#FF0000',
  'Hot_humid': '#800000',
  'Composite_1': '#FFDB58',
  'Composite_2': '#ffa700',
  'Temperate': '#00FFFF',
  'Cold': '#0A3CCF',
  '': 'pink',
};

const LEGEND_LABELS = {
  'Hot_dry': 'Hot-dry',
  'Hot_humid': 'Hot-humid',
  'Composite_1': 'Composite-dry',
  'Composite_2': 'Composite-humid',
  'Temperate': 'Temperate',
  'Cold': 'Cold',
};

export default function IndiaMapMobile({ onDistrictClick, onDistrictHover }) {
  const svgRef = useRef();
  const [climateTypes, setClimateTypes] = useState({});
  const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";

  useEffect(() => {
    fetch(`${API_URL}/api/epw/climate-types`)
      .then(res => res.json())
      .then(setClimateTypes)
      .catch(() => setClimateTypes({}));
  }, []);

  useEffect(() => {
    d3.json('/india.json').then((topology) => {
      const india = feature(topology, topology.objects.districts);
      const container = svgRef.current.parentElement;
      const width = container.offsetWidth;
      const height = container.offsetHeight;
      const projection = d3.geoMercator().fitSize([width, height], india);
      const path = d3.geoPath().projection(projection);
      const svg = d3.select(svgRef.current)
        .attr('width', width)
        .attr('height', height)
        .attr('viewBox', `0 0 ${width} ${height}`)
        .attr('preserveAspectRatio', 'xMidYMid meet');
      svg.selectAll('*').remove();
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
          if (onDistrictHover) onDistrictHover(d.properties.district, d.properties.st_nm);
        })
        .on('mouseout', function (event, d) {
          const district = (d.properties.district || '').trim();
          const state = (d.properties.st_nm || '').trim();
          const key = `${district}|${state}`;
          const climate = climateTypes[key] || '';
          d3.select(this).attr('fill', CLIMATE_COLORS[climate] || '#b3d1ff');
          if (onDistrictHover) onDistrictHover(null, null);
        })
        .on('click', function (event, d) {
          if (onDistrictClick) onDistrictClick(d.properties.district, d.properties.st_nm);
        });
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
    <div style={{ width: '100%', height: '65vh', margin: 0, padding: 0, position: 'relative' }}>
      <svg
        ref={svgRef}
        style={{ width: '100%', height: '100%', display: 'block', background: 'transparent', borderRadius: 0 }}
        preserveAspectRatio="xMidYMid meet"
      ></svg>
      <div style={{
        background: '#fff',
        border: '1px solid #ddd',
        borderRadius: 7,
        padding: '6px 4px',
        margin: '10px 0 0 0',
        boxShadow: '0 1px 4px rgba(0,0,0,0.04)',
        fontSize: 12,
        width: '100%',
        maxWidth: 340,
        display: 'block',
        zIndex: 10,
      }}>
        <b style={{ fontSize: 13, marginBottom: 6, display: 'block' }}>Climate Type Legend</b>
        {Object.entries(LEGEND_LABELS).map(([key, label]) => (
          <div key={key} style={{ display: 'flex', alignItems: 'center', marginBottom: 5 }}>
            <span style={{
              display: 'inline-block',
              width: 14,
              height: 14,
              background: CLIMATE_COLORS[key],
              border: '1px solid #bbb',
              borderRadius: 3,
              marginRight: 6,
            }}></span>
            <span style={{ fontSize: 12 }}>{label}</span>
          </div>
        ))}
      </div>
    </div>
  );
} 