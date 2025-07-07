import React from 'react';

const analysisSections = [
  {
    title: 'Weather Summary',
    text: 'Monthly values of different climate parameters.',
    img: '/Weather_File_Summary.png',
  },
  {
    title: 'Temperature Profile',
    text: 'Monthly violin curves of dry bulb temperature (DBT), wet bulb temperature (WBT), and dew point temperature (DPT).',
    img: '/Temperature_Range.png',
  },
  {
    title: 'Radiation',
    text: 'Monthly global horizontal radiation (GHR), diffuse radiation.',
    img: '/Radiation_Range.png',
  },
  {
    title: 'Air Velocity',
    text: 'Wind speeds by month – crucial for natural ventilation analysis.',
    img: '/Wind_velocity.png',
  },
  {
    title: 'Heat Maps',
    text: 'High-resolution heat maps for selected parameters (e.g., DBT, RH, etc) across the year.',
    img: '/HourlyColormap.png',
  },
  {
    title: 'Psychrometric Chart',
    text: 'Fully interactive chart showing hourly climate conditions plotted on the psychrometric space. Overlay passive strategies (like natural ventilation, evaporative cooling, thermal mass, etc.) to visualize their effectiveness and comfort potential. A predefined comfort zone based on India\'s composite climate standard is also shown.',
    img: '/Biolclimatic_Chart.png',
  },
];

export default function HowToUse() {
  return (
    <div style={{ background: '#fff', minHeight: '100vh', color: '#222', padding: '48px 0', paddingLeft: 170 }}>
      <div style={{ maxWidth: 1100, margin: '0 auto', padding: '0 24px' }}>
        <h1 style={{ fontSize: 44, fontWeight: 700, textAlign: 'center', marginBottom: 16, color: '#222' }}>
          <span role="img" aria-label="compass">🧭</span> How to Use
        </h1>
       
        <div style={{
          fontSize: 28,
          fontWeight: 700,
          margin: '48px 0 18px 0',
          color: '#1976d2',
          textAlign: 'center',
          borderBottom: '2px solid #e3e8f0',
          paddingBottom: 8,
          letterSpacing: 0.5,
        }}>1. Interactive Map Navigation</div>
        <ul style={{ fontSize: 18, marginBottom: 32, marginLeft: 0, color: '#333', textAlign: 'justify', listStyle: 'none', padding: 0 }}>
          <li style={{ display: 'flex', alignItems: 'flex-start', gap: 12, marginBottom: 12 }}>
            <span style={{ width: 14, height: 14, background: '#1976d2', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
            <span style={{ display: 'block' }}>On the front page, you'll see a detailed map of India, divided by districts.</span>
          </li>
          <li style={{ display: 'flex', alignItems: 'flex-start', gap: 12 }}>
            <span style={{ width: 14, height: 14, background: '#1976d2', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
            <span style={{ display: 'block' }}>Hover over any district to view its name, climate zone classification, and basic design conditions (e.g., dry bulb temperature, wet bulb temperature) displayed in a dynamic table on the right panel.</span>
          </li>
        </ul>
        <div style={{
          fontSize: 28,
          fontWeight: 700,
          margin: '48px 0 18px 0',
          color: '#1976d2',
          textAlign: 'center',
          borderBottom: '2px solid #e3e8f0',
          paddingBottom: 8,
          letterSpacing: 0.5,
        }}>2. District Climate Analysis</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 48, marginBottom: 32 }}>
          {analysisSections.map((section, idx) => (
            <div key={section.title} style={{
              display: 'flex',
              flexDirection: idx % 2 === 0 ? 'row' : 'row-reverse',
              alignItems: 'center',
              gap: 40,
              background: '#f7f7fa',
              borderRadius: 18,
              boxShadow: '0 2px 12px rgba(0,0,0,0.06)',
              padding: 32,
            }}>
              <img src={section.img} alt={section.title} style={{ width: 340, height: 'auto', borderRadius: 12, boxShadow: '0 2px 8px rgba(0,0,0,0.10)' }} />
              <div style={{textAlign: section.title === 'Psychrometric Chart' ? 'justify' : 'center'}}>
                <h3 style={{ fontSize: 28, fontWeight: 700, marginBottom: 10, color: '#222', textAlign: section.title === 'Psychrometric Chart' ? 'justify' : 'center' }}>{section.title}</h3>
                {section.title === 'Psychrometric Chart' ? (
                  <>
                    <p style={{ fontSize: 18, lineHeight: 1.6, color: '#444', textAlign: 'justify', marginBottom: 10 }}>
                      Fully interactive chart showing hourly climate conditions plotted on the psychrometric space. Overlay passive strategies (like natural ventilation, evaporative cooling, thermal mass, etc.) to visualize their effectiveness and comfort potential.  A predefined comfort zone based on India's composite climate standard is also shown.
                    </p>
                   
                  </>
                ) : (
                  <p style={{ fontSize: 18, lineHeight: 1.6, color: '#444', textAlign: 'center' }}>{section.text}</p>
                )}
              </div>
            </div>
          ))}
        </div>
        <div style={{
          fontSize: 28,
          fontWeight: 700,
          margin: '48px 0 18px 0',
          color: '#1976d2',
          textAlign: 'center',
          borderBottom: '2px solid #e3e8f0',
          paddingBottom: 8,
          letterSpacing: 0.5,
        }}>3. Downloads</div>
        <ul style={{ fontSize: 18, marginLeft: 0, color: '#333', textAlign: 'justify', listStyle: 'none', padding: 0 }}>
          <li style={{ display: 'flex', alignItems: 'flex-start', gap: 12, marginBottom: 12 }}>
            <span style={{ width: 14, height: 14, background: '#1976d2', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
            <span style={{ display: 'block' }}>To download data files for each district, use the <b>Download</b> tab at the top of the popup (next to "Range Plots" and "Weather File Summary").</span>
          </li>
          <ul style={{ fontSize: 17, marginLeft: 32, color: '#444', textAlign: 'justify', listStyle: 'none', padding: 0 }}>
            <li style={{ display: 'flex', alignItems: 'flex-start', gap: 10, marginBottom: 8 }}>
              <span style={{ width: 10, height: 10, background: '#90caf9', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
              <span style={{ display: 'block' }}>.epw (EnergyPlus Weather File)</span>
            </li>
            <li style={{ display: 'flex', alignItems: 'flex-start', gap: 10, marginBottom: 8 }}>
              <span style={{ width: 10, height: 10, background: '#90caf9', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
              <span style={{ display: 'block' }}>.bin (BINM file for simulation tools)</span>
            </li>
            <li style={{ display: 'flex', alignItems: 'flex-start', gap: 10 }}>
              <span style={{ width: 10, height: 10, background: '#90caf9', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
              <span style={{ display: 'block' }}>.csv (tabulated climate data)</span>
            </li>
          </ul>
        </ul>
      </div>
    </div>
  );
} 