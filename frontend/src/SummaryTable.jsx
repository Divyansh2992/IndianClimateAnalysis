import React from 'react';

const months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];

export default function SummaryTable({ summary, district }) {
  const summaryRows = [
    { label: 'Global Horizontal Radiation (avg. hr.)', key: 'ghr_avg', unit: 'W/sq.m' },
    { label: 'Direct Normal Radiation (avg. hr.)', key: 'dnr_avg', unit: 'W/sq.m' },
    { label: 'Diffuse Radiation (avg. hr.)', key: 'dhr_avg', unit: 'W/sq.m' },
    { label: 'Global Horizontal Radiation (max. hr.)', key: 'ghr_max', unit: 'W/sq.m' },
    { label: 'Direct Normal Radiation (max. hr.)', key: 'dnr_max', unit: 'W/sq.m' },
    { label: 'Diffuse Radiation (max. hr.)', key: 'dhr_max', unit: 'W/sq.m' },
    { label: 'Dry Bulb Temperature (avg. monthly)', key: 'dbt_avg', unit: 'Degree C' },
    { label: 'Dry Bulb Temperature (max.)', key: 'dbt_max', unit: 'Degree C' },
    { label: 'Dry Bulb Temperature (min.)', key: 'dbt_min', unit: 'Degree C' },
    // { label: 'Relative Humidity (avg. monthly)', key: 'rh_avg', unit: 'Percent' },
    { label: 'Wet Bulb Temperature (avg. monthly)', key: 'wbt_avg', unit: 'Degree C' },
    { label: 'Dew Point Temperature (avg. monthly)', key: 'dpt_avg', unit: 'Degree C' },
    { label: 'Wet Bulb Depression (avg. monthly)', key: 'wet_bulb_depression_avg', unit: 'Degree C' },
  ];

  return (
    <div className="container-fluid px-3 py-3">
      <h2 className="mt-0">Weather File Summary</h2>
      <div className="fw-bold mb-2">District: {district}</div>
      <div className="table-responsive">
        <table className="table table-bordered table-sm align-middle mb-0" style={{fontSize:12, minWidth:900}}>
          <thead>
            <tr>
              <th className="bg-secondary-subtle" style={{minWidth:220}}>MONTHLY MEANS</th>
              <th className="bg-secondary-subtle" style={{minWidth:70}}>Unit</th>
              {summary.map((m, i) => (
                <th key={i} className="bg-light" style={{minWidth:55, textAlign:'center'}}>{months[i]}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {summaryRows.map(row => (
              <tr key={row.key}>
                <td className="fw-bold">{row.label}</td>
                <td>{row.unit}</td>
                {summary.map((m, i) => (
                  <td key={i} style={{textAlign:'center'}}>
                    {typeof m[row.key] === 'number' && !isNaN(m[row.key]) ? (
                      ['dbt_avg', 'dbt_max', 'wbt_avg', 'dpt_avg', 'wet_bulb_depression_avg'].includes(row.key)
                        ? m[row.key].toFixed(1)
                        : Math.round(m[row.key])
                    ) : '-'}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="mt-2" style={{fontSize:12, color:'#888'}}>
        * For radiation: average values are calculated for sunshine hours
      </div>
    </div>
  );
}
