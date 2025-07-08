import React, { useState, useEffect } from 'react';
import IndiaMap from './IndiaMap';
import IndiaMapMobile from './IndiaMapMobile';

export default function ResponsiveIndiaMap(props) {
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    function handleResize() {
      setIsMobile(window.innerWidth <= 600);
    }
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  if (isMobile) {
    return <IndiaMapMobile {...props} />;
  }
  return <IndiaMap {...props} />;
} 