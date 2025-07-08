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

// Simple mobile detection hook
function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState(window.innerWidth <= 600);
  React.useEffect(() => {
    const onResize = () => setIsMobile(window.innerWidth <= 600);
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);
  return isMobile;
}

export default function HowToUse() {
  const isMobile = useIsMobile();
  return (
    <div
      style={{
        background: '#fff',
        minHeight: '100vh',
        color: '#222',
        padding: isMobile ? '24px 0 0 0' : '48px 0',
        paddingLeft: isMobile ? 0 : 170,
        width: isMobile ? '100vw' : undefined,
        boxSizing: 'border-box',
      }}
    >
      <div
        style={{
          maxWidth: isMobile ? '100%' : 1100,
          margin: '0 auto',
          padding: isMobile ? '0 8px' : '0 24px',
        }}
      >
        <h1
          style={{
            fontSize: isMobile ? 28 : 44,
            fontWeight: 700,
            textAlign: 'center',
            marginBottom: isMobile ? 10 : 16,
            color: '#222',
          }}
        >
          <span role="img" aria-label="compass">🧭</span> How to Use
        </h1>

        <div
          style={{
            fontSize: isMobile ? 20 : 28,
            fontWeight: 700,
            margin: isMobile ? '28px 0 12px 0' : '48px 0 18px 0',
            color: '#1976d2',
            textAlign: 'center',
            borderBottom: '2px solid #e3e8f0',
            paddingBottom: isMobile ? 4 : 8,
            letterSpacing: 0.5,
          }}
        >
          1. Interactive Map Navigation
        </div>
        <ul
          style={{
            fontSize: isMobile ? 15 : 18,
            marginBottom: isMobile ? 18 : 32,
            marginLeft: 0,
            color: '#333',
            textAlign: 'justify',
            listStyle: 'none',
            padding: 0,
          }}
        >
          <li style={{ display: 'flex', alignItems: 'flex-start', gap: 10, marginBottom: 10 }}>
            <span style={{ width: 12, height: 12, background: '#1976d2', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
            <span style={{ display: 'block' }}>On the front page, you'll see a detailed map of India, divided by districts.</span>
          </li>
          <li style={{ display: 'flex', alignItems: 'flex-start', gap: 10 }}>
            <span style={{ width: 12, height: 12, background: '#1976d2', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
            <span style={{ display: 'block' }}>Hover over any district to view its name, climate zone classification, and basic design conditions (e.g., dry bulb temperature, wet bulb temperature) displayed in a dynamic table on the right panel.</span>
          </li>
        </ul>
        <div
          style={{
            fontSize: isMobile ? 20 : 28,
            fontWeight: 700,
            margin: isMobile ? '28px 0 12px 0' : '48px 0 18px 0',
            color: '#1976d2',
            textAlign: 'center',
            borderBottom: '2px solid #e3e8f0',
            paddingBottom: isMobile ? 4 : 8,
            letterSpacing: 0.5,
          }}
        >
          2. District Climate Analysis
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: isMobile ? 24 : 48, marginBottom: isMobile ? 18 : 32 }}>
          {analysisSections.map((section, idx) => (
            <div
              key={section.title}
              style={{
                display: 'flex',
                flexDirection: isMobile ? 'column' : idx % 2 === 0 ? 'row' : 'row-reverse',
                alignItems: 'center',
                gap: isMobile ? 18 : 40,
                background: '#f7f7fa',
                borderRadius: 18,
                boxShadow: '0 2px 12px rgba(0,0,0,0.06)',
                padding: isMobile ? 14 : 32,
              }}
            >
              <img
                src={section.img}
                alt={section.title}
                style={{
                  width: isMobile ? '100%' : 340,
                  maxWidth: isMobile ? 320 : undefined,
                  height: 'auto',
                  borderRadius: 12,
                  boxShadow: '0 2px 8px rgba(0,0,0,0.10)',
                  marginBottom: isMobile ? 10 : 0,
                }}
              />
              <div style={{ textAlign: section.title === 'Psychrometric Chart' ? 'justify' : isMobile ? 'center' : 'center' }}>
                <h3
                  style={{
                    fontSize: isMobile ? 18 : 28,
                    fontWeight: 700,
                    marginBottom: 8,
                    color: '#222',
                    textAlign: section.title === 'Psychrometric Chart' ? 'justify' : isMobile ? 'center' : 'center',
                  }}
                >
                  {section.title}
                </h3>
                {section.title === 'Psychrometric Chart' ? (
                  <>
                    <p style={{ fontSize: isMobile ? 14 : 18, lineHeight: 1.6, color: '#444', textAlign: 'justify', marginBottom: 8 }}>
                      Fully interactive chart showing hourly climate conditions plotted on the psychrometric space. Overlay passive strategies (like natural ventilation, evaporative cooling, thermal mass, etc.) to visualize their effectiveness and comfort potential.  A predefined comfort zone based on India's composite climate standard is also shown.
                    </p>
                  </>
                ) : (
                  <p style={{ fontSize: isMobile ? 14 : 18, lineHeight: 1.6, color: '#444', textAlign: isMobile ? 'center' : 'center' }}>{section.text}</p>
                )}
              </div>
            </div>
          ))}
        </div>
        <div
          style={{
            fontSize: isMobile ? 20 : 28,
            fontWeight: 700,
            margin: isMobile ? '28px 0 12px 0' : '48px 0 18px 0',
            color: '#1976d2',
            textAlign: 'center',
            borderBottom: '2px solid #e3e8f0',
            paddingBottom: isMobile ? 4 : 8,
            letterSpacing: 0.5,
          }}
        >
          3. Downloads
        </div>
        <ul
          style={{
            fontSize: isMobile ? 15 : 18,
            marginLeft: 0,
            color: '#333',
            textAlign: 'justify',
            listStyle: 'none',
            padding: 0,
          }}
        >
          <li style={{ display: 'flex', alignItems: 'flex-start', gap: 10, marginBottom: 10 }}>
            <span style={{ width: 12, height: 12, background: '#1976d2', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
            <span style={{ display: 'block' }}>To download data files for each district, use the <b>Download</b> tab at the top of the popup (next to "Range Plots" and "Weather File Summary").</span>
          </li>
          <ul style={{ fontSize: isMobile ? 14 : 17, marginLeft: isMobile ? 18 : 32, color: '#444', textAlign: 'justify', listStyle: 'none', padding: 0 }}>
            <li style={{ display: 'flex', alignItems: 'flex-start', gap: 8, marginBottom: 6 }}>
              <span style={{ width: 9, height: 9, background: '#90caf9', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
              <span style={{ display: 'block' }}>.epw (EnergyPlus Weather File)</span>
            </li>
            <li style={{ display: 'flex', alignItems: 'flex-start', gap: 8, marginBottom: 6 }}>
              <span style={{ width: 9, height: 9, background: '#90caf9', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
              <span style={{ display: 'block' }}>.bin (BINM file for simulation tools)</span>
            </li>
            <li style={{ display: 'flex', alignItems: 'flex-start', gap: 8 }}>
              <span style={{ width: 9, height: 9, background: '#90caf9', borderRadius: '50%', display: 'inline-block', marginTop: 6, flexShrink: 0 }}></span>
              <span style={{ display: 'block' }}>.csv (tabulated climate data)</span>
            </li>
          </ul>
        </ul>
      </div>
    </div>
  );
} 