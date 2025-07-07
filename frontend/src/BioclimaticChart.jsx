import React, { useState, useEffect } from "react";

const defaultParams = {
  text: "0 - 0.5 m/s",
  comf: 1,
  epw: 1,
  evap: 1,
  thm: 1,
  sun: 1,
  active: 1,
  possible_passive: 1,
  custom_dbt: [25, 26, 27],
  custom_rh: [60, 65, 70],
  evap_efficiency: 80,
};

// Accept district as a prop
export default function BioclimaticChart({ district }) {
  const [params, setParams] = useState(defaultParams);
  const [svg, setSvg] = useState("");
  const [prevSvg, setPrevSvg] = useState("");
  const [loading, setLoading] = useState(false);

  // Fetch SVG whenever params or district changes
  useEffect(() => {
    if (district) {
      fetchSVG();
    }
    // eslint-disable-next-line
  }, [params, district]);

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    let val = type === "number" ? Number(value) : value;
    if (name === "evap_efficiency") {
      val = Math.max(0, Math.min(100, val));
    }
    setParams((prev) => ({
      ...prev,
      [name]: val,
    }));
  };

  const handleRadio = (e) => {
    setParams((prev) => ({
      ...prev,
      text: e.target.value,
    }));
  };

  const toggleStrategy = (key) => {
    setParams(prev => {
      const newParams = { ...prev, [key]: prev[key] ? 0 : 1 };
      return newParams;
    });
  };

  const fetchSVG = async (customParams) => {
    setLoading(true);
    setPrevSvg(svg); // Save current SVG before loading new one
    // setSvg(""); // Don't clear svg immediately
    const body = { ...(customParams || params), district };
    const response = await fetch("http://localhost:3000/api/epw/psychrometry/save-svg", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    const svgText = await response.text();
    setSvg(svgText);
    setLoading(false);
  };

  const monthOptions = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ];
  const hourOptions = Array.from({ length: 24 }, (_, i) => i + 1);
  const dayOptions = Array.from({ length: 31 }, (_, i) => i + 1);

  const periodPresets = {
    Annual: { fromMonth: 'January', toMonth: 'December', fromDay: 1, toDay: 31, fromHour: 1, toHour: 24, disable: true },
    Summer: { fromMonth: 'April', toMonth: 'June', fromDay: 1, toDay: 30, fromHour: 1, toHour: 24, disable: true },
    Winter: { fromMonth: 'December', toMonth: 'February', fromDay: 1, toDay: 31, fromHour: 1, toHour: 24, disable: true },
    Monsoon: { fromMonth: 'July', toMonth: 'September', fromDay: 1, toDay: 15, fromHour: 1, toHour: 24, disable: true },
    Spring: { fromMonth: 'February', toMonth: 'March', fromDay: 1, toDay: 31, fromHour: 1, toHour: 24, disable: true },
    Autumn: { fromMonth: 'September', toMonth: 'November', fromDay: 16, toDay: 30, fromHour: 1, toHour: 24, disable: true },
    Custom: { disable: false }
  };
  const [selectedPeriod, setSelectedPeriod] = useState('Annual');

  const handlePeriodChange = (e) => {
    const period = e.target.value;
    setSelectedPeriod(period);
    if (periodPresets[period]) {
      setParams(p => ({
        ...p,
        ...periodPresets[period]
      }));
    }
  };

  return (
    <>
      <div className="container-fluid px-2 py-2" style={{background: 'transparent', fontFamily: "'Segoe UI', Arial, sans-serif", overflow: 'hidden', paddingTop: '8px', marginTop: '-10px'}}>
        <div className="row align-items-start g-0" style={{marginTop: '-10px'}}>
          {/* Time, Efficiency, Air Velocity */}
          <div className="col-12 col-lg-3 mb-3 mb-lg-0">
            <div className="bg-white rounded-2 border p-3 h-100">
              <h2 className="fw-bold mb-2" style={{ fontSize: 16, letterSpacing: 0.5 }}>Bioclimatic Design Chart</h2>
              {/* Time Section */}
              <div className="mb-2">
                <b className="text-secondary" style={{ fontSize: 11 }}>TIME</b>
                <div className="mb-2 mt-1">
                  <label className="fw-medium me-1" style={{ fontSize: 11 }}>Period:</label>
                  <select value={selectedPeriod} onChange={handlePeriodChange} className="form-select form-select-sm d-inline-block w-auto" style={{ fontSize: 11, padding: '1px 4px', borderRadius: 4 }}>
                    {Object.keys(periodPresets).map(period => (
                      <option key={period} value={period}>{period}</option>
                    ))}
                  </select>
                </div>
                <div className="d-flex flex-column gap-1 mt-1">
                  <div className="mb-1">
                    <label style={{ fontSize: 10 }}>MONTH :</label>
                    <div className="d-flex gap-1 mt-1">
                      <select name="fromMonth" value={params.fromMonth || 'January'} onChange={e => setParams(p => ({ ...p, fromMonth: e.target.value }))} disabled={periodPresets[selectedPeriod].disable} className="form-select form-select-sm w-auto" style={{ fontSize: 10, borderRadius: 3 }}>
                        {monthOptions.map(m => <option key={m} value={m}>{m}</option>)}
                      </select>
                      <span className="fw-medium mx-1" style={{ fontSize: 10 }}>to</span>
                      <select name="toMonth" value={params.toMonth || 'December'} onChange={e => setParams(p => ({ ...p, toMonth: e.target.value }))} disabled={periodPresets[selectedPeriod].disable} className="form-select form-select-sm w-auto" style={{ fontSize: 10, borderRadius: 3 }}>
                        {monthOptions.map(m => <option key={m} value={m}>{m}</option>)}
                      </select>
                    </div>
                  </div>
                  <div className="mb-1">
                    <label style={{ fontSize: 10 }}>DAY :</label>
                    <div className="d-flex gap-1 mt-1">
                      <select name="fromDay" value={params.fromDay || 1} onChange={e => setParams(p => ({ ...p, fromDay: Number(e.target.value) }))} disabled={periodPresets[selectedPeriod].disable} className="form-select form-select-sm w-auto" style={{ fontSize: 10, borderRadius: 3 }}>
                        {dayOptions.map(d => <option key={d} value={d}>{d}</option>)}
                      </select>
                      <span className="fw-medium mx-1" style={{ fontSize: 10 }}>to</span>
                      <select name="toDay" value={params.toDay || 31} onChange={e => setParams(p => ({ ...p, toDay: Number(e.target.value) }))} disabled={periodPresets[selectedPeriod].disable} className="form-select form-select-sm w-auto" style={{ fontSize: 10, borderRadius: 3 }}>
                        {dayOptions.map(d => <option key={d} value={d}>{d}</option>)}
                      </select>
                    </div>
                  </div>
                  <div>
                    <label style={{ fontSize: 10 }}>HOUR :</label>
                    <div className="d-flex gap-1 mt-1">
                      <select name="fromHour" value={params.fromHour || 1} onChange={e => setParams(p => ({ ...p, fromHour: Number(e.target.value) }))} disabled={periodPresets[selectedPeriod].disable} className="form-select form-select-sm w-auto" style={{ fontSize: 10, borderRadius: 3 }}>
                        {hourOptions.map(h => <option key={h} value={h}>{h}</option>)}
                      </select>
                      <span className="fw-medium mx-1" style={{ fontSize: 10 }}>to</span>
                      <select name="toHour" value={params.toHour || 24} onChange={e => setParams(p => ({ ...p, toHour: Number(e.target.value) }))} disabled={periodPresets[selectedPeriod].disable} className="form-select form-select-sm w-auto" style={{ fontSize: 10, borderRadius: 3 }}>
                        {hourOptions.map(h => <option key={h} value={h}>{h}</option>)}
                      </select>
                    </div>
                  </div>
                </div>
              </div>
              <div className="border-top my-2" style={{ borderColor: '#ddd' }} />
              {/* Efficiency + Air Velocity Section */}
              <div className="mb-3 mb-lg-4" style={{ padding: '2px 0', borderBottom: '1px solid #ddd' }}>
                {/* Efficiency */}
                <div className="mb-2">
                  <label htmlFor="evap-efficiency" className="fw-medium" style={{ fontSize: 12, color: '#333' }}>
                    Evap. cooler Efficiency (%)
                  </label>
                  <input
                    type="number"
                    id="evap-efficiency"
                    name="evap_efficiency"
                    min={0}
                    max={100}
                    value={params.evap_efficiency}
                    onChange={handleChange}
                    className="form-control form-control-sm"
                    style={{ width: 48, fontSize: 12, display: 'inline-block', marginLeft: 8 }}
                  />
                </div>
                {/* Air Velocity */}
                <div>
                  <b className="fw-medium" style={{ fontSize: 12, color: '#444', display: 'block', marginBottom: 2 }}>Air Velocity</b>
                  <div className="d-flex flex-column gap-2">
                    {['0 - 0.5 m/s', '0.5 - 1.0 m/s', '1.0 - 1.5 m/s'].map((val) => (
                      <label key={val} className="d-flex align-items-center font-size-12" style={{ background: params.text === val ? '#e3f0ff' : '#f5f5f5', color: '#1976d2', border: '1px solid #1976d2', borderRadius: 3, padding: '2px 6px', fontWeight: 500, cursor: 'pointer', marginBottom: 0 }}>
                        <input type="radio" name="text" value={val} checked={params.text === val} onChange={handleRadio} className="form-check-input me-2" style={{ marginRight: 6 }} />
                        {val}
                      </label>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>
          {/* Design Strategies */}
          <div className="col-12 col-lg-4 mb-2 mb-lg-0 h-100" style={{ minWidth: 180, zIndex: 2, maxWidth: 260 }}>
            <div className="bg-white rounded-2 border p-1 h-100" style={{ fontSize: '0.95rem' }}>
              <b className="fw-bold" style={{ fontSize: '1rem' }}>Select Design Strategies</b>
              <div className="d-flex flex-column gap-1 mt-2">
                <div className="bg-light text-dark border border-secondary rounded-3 p-2 cursor-pointer d-inline-flex align-items-center w-auto mb-1" onClick={() => toggleStrategy('comf')} style={{ opacity: params.comf ? 1 : 0.5, fontSize: 10 }}>
                  <span className="d-inline-block me-2" style={{ width: 16, height: 16, background: '#2196f3', borderRadius: 3 }}></span>
                  Comfortable Outdoor Conditions
                </div>
                <div className="bg-light text-dark border border-secondary rounded-3 p-2 cursor-pointer d-inline-flex align-items-center w-auto mb-1" onClick={() => toggleStrategy('evap')} style={{ opacity: params.evap ? 1 : 0.5, fontSize: 10 }}>
                  <span className="d-inline-block me-2" style={{ width: 16, height: 16, background: '#43a047', borderRadius: 3 }}></span>
                  Evaporative cooling
                </div>
                <div className="bg-light text-dark border border-secondary rounded-3 p-2 cursor-pointer d-inline-flex align-items-center w-auto mb-1" onClick={() => toggleStrategy('thm')} style={{ opacity: params.thm ? 1 : 0.5, fontSize: 10 }}>
                  <span className="d-inline-block me-2" style={{ width: 16, height: 16, background: '#ffe082', borderRadius: 3 }}></span>
                  Thermal mass
                </div>
                <div className="bg-light text-dark border border-secondary rounded-3 p-2 cursor-pointer d-inline-flex align-items-center w-auto mb-1" onClick={() => toggleStrategy('sun')} style={{ opacity: params.sun ? 1 : 0.5, fontSize: 10 }}>
                  <span className="d-inline-block me-2" style={{ width: 16, height: 16, background: '#ff9800', borderRadius: 3 }}></span>
                  Sun shading
                </div>
                <div className="bg-light text-dark border border-secondary rounded-3 p-2 cursor-pointer d-inline-flex align-items-center w-auto mb-1" onClick={() => toggleStrategy('active')} style={{ opacity: params.active ? 1 : 0.5, fontSize: 10 }}>
                  <span className="d-inline-block me-2" style={{ width: 16, height: 16, background: '#e53935', borderRadius: 3 }}></span>
                  Active Cooling/Heating/Dehum
                </div>
                <div className="bg-light text-dark border border-secondary rounded-3 p-2 cursor-pointer d-inline-flex align-items-center w-auto mb-1" onClick={() => toggleStrategy('possible_passive')} style={{ opacity: params.possible_passive ? 1 : 0.5, fontSize: 10 }}>
                  <span className="d-inline-block me-2" style={{ width: 16, height: 16, background: '#90caf9', borderRadius: 3 }}></span>
                  Possible Comfort hours (passive)
                </div>
              </div>
            </div>
          </div>
          {/* Loading indicator */}
          <div className="col-12 col-lg-1 d-flex justify-content-center align-items-center mb-2" style={{ minWidth: 80, zIndex: 999, position: 'relative' }}>
            {loading ? (
              <button className="btn btn-primary d-flex align-items-center gap-2 px-3 py-1" type="button" disabled style={{ fontSize: 15, fontWeight: 500, opacity: 0.95 }}>
                <span className="spinner-border spinner-border-sm text-light" role="status" style={{ width: 18, height: 18, borderWidth: 2}} />
                Loading...
              </button>
            ) : (
              <div style={{ width: '100%', height: '32px', visibility: 'hidden' }}></div>
            )}
          </div>
          {/* Chart Area */}
          <div className="col-12 col-lg-4 ps-0 h-100" style={{ minWidth: 400, zIndex: 1, maxHeight: '100%', padding: 0, margin: 0 }}>
            <div className="h-100" style={{ minHeight: 320, maxHeight: '100%', padding: 0, margin: 0, marginLeft: '12px' }}>
              {(svg || prevSvg) ? (
                <div className="h-100 d-flex align-items-center justify-content-center">
                  <div className="h-100 d-flex align-items-center justify-content-center"
                    dangerouslySetInnerHTML={{ __html: loading && prevSvg ? prevSvg : svg }} />
                </div>
              ) : (
                <div className="h-100 d-flex align-items-center justify-content-center">
                  <span className="text-secondary" style={{ fontSize: 18 }}>Chart will appear here</span>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
