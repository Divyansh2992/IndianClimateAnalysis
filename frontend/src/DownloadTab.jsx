import React, { useState, useRef } from 'react';

const FILE_FORMATS = [
  { label: 'EPW file', value: 'epw' },
  { label: 'BIN file', value: 'bin' },
  { label: 'CSV file', value: 'csv' },
];

function getDownloadUrl(district, format) {
  if (!district) return '#';
  if (format === 'epw') {
    return `/api/epw/download/district/${encodeURIComponent(district)}`;
  }
  if (format === 'csv') {
    return `/api/epw/download-csv/district/${encodeURIComponent(district)}`;
  }
  if (format === 'bin') {
    return `/api/epw/download-bin/district/${encodeURIComponent(district)}`;
  }
  // Add endpoints for other formats as needed
  return '#';
}

const DownloadTab = ({ district }) => {
  const [format, setFormat] = useState('epw');
  const [downloading, setDownloading] = useState(false);
  const anchorRef = useRef(null);

  const handleDownload = async (e) => {
    e.preventDefault();
    if (!district) return;
    setDownloading(true);
    const url = getDownloadUrl(district, format);
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error('Download failed');
      const blob = await response.blob();
      const contentDisposition = response.headers.get('Content-Disposition');
      let filename = `${district}.${format}`;
      if (contentDisposition) {
        const match = contentDisposition.match(/filename="?([^";]+)"?/);
        if (match) filename = match[1];
      }
      const blobUrl = window.URL.createObjectURL(blob);
      const a = anchorRef.current;
      a.href = blobUrl;
      a.download = filename;
      a.click();
      setTimeout(() => {
        window.URL.revokeObjectURL(blobUrl);
      }, 2000);
    } catch {
      alert('Failed to download file.');
    } finally {
      setDownloading(false);
    }
  };

  return (
    <div className="container py-4 px-2" style={{ minWidth: 220, maxWidth: 600 }}>
      <h3 className="mb-4">Download Weather Data</h3>
      <form className="row g-3 align-items-center mb-3" onSubmit={handleDownload}>
        <div className="col-12 col-md-6 mb-2 mb-md-0">
          <label className="form-label fw-semibold me-2">File Format:</label>
          <select value={format} onChange={e => setFormat(e.target.value)} className="form-select d-inline-block w-auto" style={{ fontSize: 15 }}>
            {FILE_FORMATS.map(f => (
              <option key={f.value} value={f.value}>{f.label}</option>
            ))}
          </select>
        </div>
        <div className="col-12 col-md-6">
          <label className="form-label fw-semibold me-2">District:</label>
          <span className="fs-6">{district || <span className="text-danger">Select a district on the map</span>}</span>
        </div>
        <div className="col-12 mt-2">
          <button
            type="submit"
            disabled={!district || downloading}
            className={`btn btn-primary px-4 py-2 fw-semibold fs-5${(!district || downloading) ? ' disabled' : ''}`}
            style={{ borderRadius: 6, minWidth: 120 }}
          >
            {downloading ? (
              <span className="d-flex align-items-center gap-2">
                <span className="spinner-border spinner-border-sm text-light" role="status" style={{ width: 18, height: 18, borderWidth: 2 }} />
                Downloading...
              </span>
            ) : 'Download'}
          </button>
          <a ref={anchorRef} style={{ display: 'none' }}>Download</a>
        </div>
      </form>
    </div>
  );
};

export default DownloadTab; 