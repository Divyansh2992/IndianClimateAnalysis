import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SummaryTable from './SummaryTable';
import IndiaMap from './IndiaMap';
import TemperatureViolinPlot from './TemperatureViolinPlot';
import RadiationViolinPlot from './RadiationViolinPlot';
import WindVelocityViolinPlot from './WindVelocityViolinPlot';
import GroundTemperatureLinePlot from './GroundTemperatureLinePlot';
import HourlyColormapPlot from './HourlyColormapPlot';
import BioclimaticChart from './BioclimaticChart';
import DownloadTab from './DownloadTab';
import VerticalNavbar from './VerticalNavbar';
import './VerticalNavbar.css';
import HowToUse from './HowToUse';
import About from './About';

const VAR_LABELS = {
  dryBulb: 'DBT',
  wetBulb: 'WB',
  meanCoincidentDryBulb: 'MCDB',
  mcwb: 'MCWB',
  mcdb: 'MCDB',
  wb: 'WB',
  dbt: 'DBT',
  // Add more mappings as needed
};

const VAR_SHORT_FORM = {
  dryBulb: 'DBT',
  wetBulb: 'MCWB',
  meanCoincidentDryBulb: 'MCDB',
  mcwb: 'MCWB',
  mcdb: 'MCDB',
  wb: 'MCWB',
  dbt: 'DBT',
  wetbulb: 'MCWB',
  drybulb: 'DBT',
  meancoincidentdrybulb: 'MCDB',
  // Add more as needed
};

function MainAppContent() {
  const [popup, setPopup] = useState({ visible: false, district: '', summary: null });
  const [activeTab, setActiveTab] = useState('summary');
  const [activeSubTab, setActiveSubTab] = useState('temperature');
  const [hoveredDistrict, setHoveredDistrict] = useState(null);
  const [designConditions, setDesignConditions] = useState(null);
  const [designSource, setDesignSource] = useState(null);
  const [degreeDays, setDegreeDays] = useState(null);
  const [isMobile, setIsMobile] = useState(window.innerWidth < 576);
  const [isTablet, setIsTablet] = useState(window.innerWidth < 768);

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 576);
      setIsTablet(window.innerWidth < 768);
    };
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const handleDistrictClick = (district) => {
    fetch(`/api/epw/summary/district/${encodeURIComponent(district)}`)
      .then(async res => {
        if (!res.ok) {
          throw new Error('Not found');
        }
        const data = await res.json();
        if (!data.summary) {
          throw new Error('No summary');
        }
        setPopup({ visible: true, district, summary: data.summary });
      })
      .catch((err) => {
        console.error('EPW fetch error:', err);
        setPopup({ visible: true, district, summary: null });
      });
  };

  const handleDistrictHover = (districtName, stateName) => {
    setHoveredDistrict(districtName);
    if (districtName && stateName) {
      const normDistrict = districtName.trim().toLowerCase();
      const normState = stateName.trim().toLowerCase();
      fetch(`http://localhost:3000/api/epw/design-conditions/${encodeURIComponent(normDistrict)}/${encodeURIComponent(normState)}`)
        .then(res => {
          if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
          }
          return res.json();
        })
        .then(data => {
          setDesignConditions(data.designConditions);
          setDesignSource(data.source);
          setDegreeDays(data.degreeDays || null);
        })
        .catch(error => {
          console.error('Error fetching design conditions:', error);
          setDesignConditions(null);
          setDesignSource(null);
          setDegreeDays(null);
        });
    } else {
      setDesignConditions(null);
      setDesignSource(null);
      setDegreeDays(null);
    }
  };

  const subtabStyle = (tab) => ({
    padding: '6px 24px 6px 0',
    fontWeight: 600,
    fontSize: 15,
    borderBottom: activeSubTab === tab ? '2px solid #1976d2' : '2px solid transparent',
    color: activeSubTab === tab ? '#1976d2' : '#222',
    cursor: 'pointer',
    marginRight: 8,
    background: 'none',
    minWidth: 120,
  });

  return (
    <>
      <div style={{
        width: '100%',
        textAlign: 'center',
        fontSize: 44,
        fontWeight: 700,
        letterSpacing: 1,
        marginBottom: 0,
        marginTop: 2,
        fontFamily: `'Playfair Display', 'Merriweather', 'Georgia', serif`,
        color: '#1a237e',
        textShadow: '0 2px 8px rgba(26,35,126,0.08)',
      }}>
        Indian Weather Analysis
      </div>
      <div
        className="main-flex-container"
        style={{
          position: 'relative',
          background: isMobile || isTablet ? '#fff' : '#f5f5f5',
          minHeight: isMobile || isTablet ? 'unset' : 595,
          height: isMobile || isTablet ? 'unset' : undefined,
          padding: isMobile ? '8px 0 0 0' : isTablet ? '16px 8px 0 8px' : '32px 32px 0 32px',
          display: 'flex',
          flexDirection: isMobile || isTablet ? 'column' : 'row',
          marginLeft: isMobile ? 0 : 90,
          overflow: isMobile || isTablet ? 'visible' : 'hidden',
        }}
      >
        <div style={{ flex: 1, marginRight: isMobile || isTablet ? 0 : 20, width: isMobile || isTablet ? '100vw' : '100%' }}>
          <IndiaMap onDistrictClick={handleDistrictClick} onDistrictHover={isMobile ? undefined : handleDistrictHover} />
          {/* Tooltip is not shown on mobile */}
          {!isMobile && (
            <div id="tooltip" style={{
              position: 'absolute',
              display: 'none',
              pointerEvents: 'none',
              background: 'rgba(0,0,0,0.8)',
              color: '#fff',
              padding: '4px 8px',
              borderRadius: '4px',
              fontSize: '14px',
              zIndex: 10
            }}></div>
          )}
        </div>
        {/* Right side panel for Design Conditions - hidden on mobile/tablet */}
        {!(isMobile || isTablet) && (
          <div
            className="design-conditions-panel"
            style={{
              width: 400,
              background: '#fff',
              borderRadius: 8,
              padding: '24px 16px 8px 16px',
              display: 'inline-block',
              boxSizing: 'border-box',
              marginBottom: 0,
              height: '600px',
              marginTop: -18,
            }}
          >
            <h2 style={{ fontSize: 24, marginBottom: 20, textAlign: 'center' }}>Design Conditions</h2>
            {hoveredDistrict ? (
              designConditions ? (
                <div>
                  <h3 style={{ fontSize: 18, marginBottom: 10, textAlign: 'center' }}>{hoveredDistrict}{designSource ? ` (${designSource})` : ''}</h3>
                  {/* CDD/HDD Section */}
                  {degreeDays && (degreeDays.CDD || degreeDays.HDD) && (
                    <div style={{ margin: '10px 0 18px 0', padding: '10px 0', borderTop: '1px solid #eee', borderBottom: '1px solid #eee', textAlign: 'center' }}>
                      {degreeDays.CDD !== null && (
                        <span style={{ marginRight: 16 }}>CDD(18&#176;C): <span style={{ fontWeight: 500 }}>{degreeDays.CDD}</span></span>
                      )}
                      {degreeDays.HDD !== null && (
                        <span>HDD(18&#176;C): <span style={{ fontWeight: 500 }}>{degreeDays.HDD}</span></span>
                      )}
                    </div>
                  )}
                  {/* Heating Table */}
                  {designConditions.Heating && (
                    <div style={{ marginBottom: 15 }}>
                      <h4 style={{ fontSize: 16, marginBottom: 8, borderBottom: '1px solid #eee', paddingBottom: 3 }}>Heating(&#176;C)</h4>
                      <div style={{ overflowX: 'auto' }}>
                        <table className="table table-sm" style={{ width: '100%', borderCollapse: 'collapse', minWidth: 350 }}>
                          <thead>
                            <tr>
                              <th style={{ border: '1px solid #ddd', padding: 5, background: '#f2f2f2', fontSize: 13 }}>Variable</th>
                              {Object.keys(designConditions.Heating).map(percentage => (
                                <th key={percentage} style={{ border: '1px solid #ddd', padding: 5, textAlign: 'left', background: '#f2f2f2', fontSize: 13 }}>{percentage}</th>
                              ))}
                            </tr>
                          </thead>
                          <tbody>
                            {Object.keys(designConditions.Heating[Object.keys(designConditions.Heating)[0]]).map(varKey => (
                              <tr key={varKey}>
                                <td style={{ border: '1px solid #ddd', padding: 5, fontSize: 12 }}>{VAR_SHORT_FORM[varKey.toLowerCase()] || varKey}</td>
                                {Object.keys(designConditions.Heating).map(percentage => (
                                  <td key={percentage} style={{ border: '1px solid #ddd', padding: 5, fontSize: 12 }}>{designConditions.Heating[percentage][varKey]}</td>
                                ))}
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}
                  {/* Cooling Table */}
                  {designConditions.Cooling && (
                    <div style={{ marginBottom: 15 }}>
                      <h4 style={{ fontSize: 16, marginBottom: 8, borderBottom: '1px solid #eee', paddingBottom: 3 }}>Cooling(&#176;C)</h4>
                      <div style={{ overflowX: 'auto' }}>
                        <table className="table table-sm" style={{ width: '100%', borderCollapse: 'collapse', minWidth: 350 }}>
                          <thead>
                            <tr>
                              <th style={{ border: '1px solid #ddd', padding: 5, background: '#f2f2f2', fontSize: 13 }}>Variable</th>
                              {Object.keys(designConditions.Cooling).map(percentage => (
                                <th key={percentage} style={{ border: '1px solid #ddd', padding: 5, textAlign: 'left', background: '#f2f2f2', fontSize: 13 }}>{percentage}</th>
                              ))}
                            </tr>
                          </thead>
                          <tbody>
                            {Object.keys(designConditions.Cooling[Object.keys(designConditions.Cooling)[0]]).map(varKey => (
                              <tr key={varKey}>
                                <td style={{ border: '1px solid #ddd', padding: 5, fontSize: 12 }}>{VAR_SHORT_FORM[varKey.toLowerCase()] || varKey}</td>
                                {Object.keys(designConditions.Cooling).map(percentage => (
                                  <td key={percentage} style={{ border: '1px solid #ddd', padding: 5, fontSize: 12 }}>{designConditions.Cooling[percentage][varKey]}</td>
                                ))}
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}
                  {/* Evaporation Table */}
                  {designConditions.Evaporation && (
                    <div style={{ marginBottom: 15 }}>
                      <h4 style={{ fontSize: 16, marginBottom: 8, borderBottom: '1px solid #eee', paddingBottom: 3 }}>Evaporation(&#176;C)</h4>
                      <div style={{ overflowX: 'auto' }}>
                        <table className="table table-sm" style={{ width: '100%', borderCollapse: 'collapse', minWidth: 350 }}>
                          <thead>
                            <tr>
                              <th style={{ border: '1px solid #ddd', padding: 5, background: '#f2f2f2', fontSize: 13 }}>Variable</th>
                              {Object.keys(designConditions.Evaporation).map(percentage => (
                                <th key={percentage} style={{ border: '1px solid #ddd', padding: 5, textAlign: 'left', background: '#f2f2f2', fontSize: 13 }}>{percentage}</th>
                              ))}
                            </tr>
                          </thead>
                          <tbody>
                            {Object.keys(designConditions.Evaporation[Object.keys(designConditions.Evaporation)[0]]).map(varKey => (
                              <tr key={varKey}>
                                <td style={{ border: '1px solid #ddd', padding: 5, fontSize: 12 }}>{VAR_SHORT_FORM[varKey.toLowerCase()] || varKey}</td>
                                {Object.keys(designConditions.Evaporation).map(percentage => (
                                  <td key={percentage} style={{ border: '1px solid #ddd', padding: 5, fontSize: 12 }}>{designConditions.Evaporation[percentage][varKey]}</td>
                                ))}
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}
                </div>
              ) : (
                <p style={{ textAlign: 'center', color: '#666' }}>Fetching design conditions for {hoveredDistrict}...</p>
              )
            ) : (
              <p style={{ textAlign: 'center', color: '#666' }}>Hover over a district on the map to see its design conditions.</p>
            )}
          </div>
        )}
      </div>
      {popup.visible && (
        <div style={{
          position: 'fixed',
          top: 0, left: 0, right: 0, bottom: 0,
          background: 'rgba(0,0,0,0.25)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1000,
          padding: isMobile ? 0 : '32px',
          boxSizing: 'border-box',
          overflowX: 'visible',
        }} onClick={() => setPopup({ ...popup, visible: false })}>
          <div style={{
            background: '#fff',
            borderRadius: isMobile ? 0 : 12,
            padding: 0,
            width: isMobile ? '100vw' : '95%',
            maxWidth: isMobile ? '100vw' : 1200,
            maxHeight: isMobile ? '100vh' : '90vh',
            minHeight: isMobile ? '100vh' : undefined,
            boxShadow: '0 8px 32px rgba(0,0,0,0.12)',
            position: 'relative',
            cursor: 'auto',
            border: '1px solid #e0e6ef',
            display: 'flex',
            flexDirection: 'column',
            boxSizing: 'border-box',
            fontSize: isMobile ? 14 : 15,
            overflowY: 'auto',
            overflowX: 'visible',
          }} onClick={e => e.stopPropagation()}>
            {/* Top Tabs */}
            <div style={{
              borderBottom: '1px solid #e0e6ef',
              padding: isMobile ? '0 8px' : '0 24px',
              display: 'flex',
              gap: isMobile ? 8 : 24,
              userSelect: 'none',
              flexDirection: isMobile ? 'column' : 'row',
              alignItems: isMobile ? 'stretch' : 'center',
            }}>
              {['Weather File Summary', 'Range Plots', 'Download'].map((tab, i) => (
                <div
                  key={i}
                  onClick={() => {
                    if (i === 0) setActiveTab('summary');
                    else if (i === 1) setActiveTab('range');
                    else setActiveTab('download');
                  }}
                  style={{
                    padding: isMobile ? '12px 4px' : '16px 8px',
                    cursor: 'pointer',
                    color: activeTab === (i === 0 ? 'summary' : i === 1 ? 'range' : 'download') ? '#000' : '#666',
                    borderBottom: `2px solid ${activeTab === (i === 0 ? 'summary' : i === 1 ? 'range' : 'download') ? '#007AFF' : 'transparent'}`,
                    transition: 'all 0.2s',
                    fontWeight: activeTab === (i === 0 ? 'summary' : i === 1 ? 'range' : 'download') ? 500 : 400,
                    textAlign: isMobile ? 'center' : 'left',
                  }}
                >
                  {tab}
                </div>
              ))}
            </div>
            {/* Content */}
            <div style={{
              padding: isMobile ? 8 : 0,
              paddingBottom: 0,
              overflowY: 'auto',
              flex: 1,
              minHeight: 0,
              position: 'relative',
              maxHeight: isMobile ? 'calc(100vh - 60px)' : undefined,
            }}>
              {activeTab === 'summary' ? (
                popup.summary ? (
                  <SummaryTable summary={popup.summary} district={popup.district} />
                ) : (
                  <div className="d-flex flex-column align-items-center justify-content-center" style={{minHeight: '300px', padding: '40px 20px'}}>
                    <div className="text-center">
                      <h3 className="text-danger mb-2" style={{fontWeight:600, fontSize:'1.5rem'}}>Weather data not available for {popup.district}.</h3>
                    </div>
                  </div>
                )
              ) : activeTab === 'range' ? (
                popup.summary ? (
                  <>
                    <div style={{ display: 'flex', alignItems: 'center', borderBottom: '1px solid #e0e0e0', marginBottom: 20, padding: '0 16px' }}>
                      <div
                        onClick={() => setActiveSubTab('temperature')}
                        style={subtabStyle('temperature')}
                      >
                        Temperature Range
                      </div>
                      <div
                        onClick={() => setActiveSubTab('radiation')}
                        style={subtabStyle('radiation')}
                      >
                        Radiation Range
                      </div>
                      <div
                        onClick={() => setActiveSubTab('wind')}
                        style={subtabStyle('wind')}
                      >
                        Air Velocity Range
                      </div>
                      <div
                        onClick={() => setActiveSubTab('ground')}
                        style={subtabStyle('ground')}
                      >
                        Ground Temperature
                      </div>
                      <div
                        onClick={() => setActiveSubTab('hourlycolormap')}
                        style={subtabStyle('hourlycolormap')}
                      >
                        Hourly Heatmap
                      </div>
                      <div
                        onClick={() => setActiveSubTab('bioclimatic')}
                        style={subtabStyle('bioclimatic')}
                      >
                        Bioclimatic Chart
                      </div>
                    </div>
                    <div style={{ flex: 1, display: 'flex', flexDirection: 'column', padding: '6px 0 6px 0', }}>
                      {activeSubTab === 'temperature' ? (
                        <TemperatureViolinPlot district={popup.district} />
                      ) : activeSubTab === 'radiation' ? (
                        <RadiationViolinPlot district={popup.district} />
                      ) : activeSubTab === 'wind' ? (
                        <WindVelocityViolinPlot district={popup.district} />
                      ) : activeSubTab === 'ground' ? (
                        <GroundTemperatureLinePlot district={popup.district} />
                      ) : activeSubTab === 'hourlycolormap' ? (
                        <HourlyColormapPlot district={popup.district} />
                      ) : (
                        <BioclimaticChart district={popup.district} />
                      )}
                    </div>
                  </>
                ) : (
                  <div className="d-flex flex-column align-items-center justify-content-center" style={{minHeight: '300px', padding: '40px 20px'}}>
                    <div className="text-center">
                      <h3 className="text-danger mb-2" style={{fontWeight:600, fontSize:'1.5rem'}}>Weather data not available for {popup.district}.</h3>
                    </div>
                  </div>
                )
              ) : (
                popup.summary ? (
                  <DownloadTab district={popup.district} />
                ) : (
                  <div className="d-flex flex-column align-items-center justify-content-center" style={{minHeight: '300px', padding: '40px 20px'}}>
                    <div className="text-center">
                      <h3 className="text-danger mb-2" style={{fontWeight:600, fontSize:'1.5rem'}}>Weather data not available for {popup.district}.</h3>
                    </div>
                  </div>
                )
              )}
            </div>
            {/* Close Button at Top Right */}
            <button 
              onClick={() => setPopup({ ...popup, visible: false })}
              style={{
                position: 'absolute',
                right: 16,
                top: 16,
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                padding: 8,
                borderRadius: 4,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#666',
                zIndex: 10,
              }}
            >
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path d="M12.5 3.5L3.5 12.5M3.5 3.5L12.5 12.5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
              </svg>
            </button>
          </div>
        </div>
      )}
      {/* Responsive styles for tables/charts in popup */}
      <style>{`
        @media (max-width: 767px) {
          .main-flex-container { flex-direction: column !important; padding: 8px 0 0 0 !important; margin-left: 0 !important; }
          .design-conditions-panel { width: 100vw !important; height: auto !important; min-height: unset !important; margin-top: 0 !important; border-radius: 0 !important; padding: 12px 4px 8px 4px !important; }
          .main-flex-container > div { width: 100vw !important; margin-right: 0 !important; }
          .main-flex-container svg { width: 100vw !important; height: auto !important; }
        }
        @media (max-width: 575px) {
          .main-flex-container { flex-direction: column !important; padding: 4px 0 0 0 !important; margin-left: 0 !important; }
          .design-conditions-panel { width: 100vw !important; height: auto !important; min-height: unset !important; margin-top: 0 !important; border-radius: 0 !important; padding: 8px 2px 6px 2px !important; }
          .main-flex-container > div { width: 100vw !important; margin-right: 0 !important; }
          .main-flex-container svg { width: 100vw !important; height: auto !important; }
        }
      `}</style>
    </>
  );
}

function App() {
  return (
    <Router>
      <VerticalNavbar />
      <Routes>
        <Route path="/" element={<MainAppContent />} />
        <Route path="/how-to-use" element={<HowToUse />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;
