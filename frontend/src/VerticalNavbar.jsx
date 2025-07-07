import React, { useState } from "react";
import { Home, Info, HelpCircle, Menu } from "react-feather";
import { Link } from 'react-router-dom';
import "./VerticalNavbar.css";

const navItems = [
  { icon: <Home size={28} />, label: "Home", to: "/" },
  { icon: <Info size={28} />, label: "About Us", to: "/about" },
  { icon: <HelpCircle size={28} />, label: "How to Use", to: "/how-to-use" },
];

export default function VerticalNavbar() {
  const [open, setOpen] = useState(false);

  // Close menu on navigation (for mobile)
  const handleNavClick = () => setOpen(false);

  return (
    <>
      {/* Hamburger button for mobile/tablet */}
      <button
        className="vertical-navbar__hamburger"
        aria-label={open ? "Close menu" : "Open menu"}
        onClick={() => setOpen((v) => !v)}
      >
        <Menu size={32} />
      </button>
      {/* Overlay for mobile/tablet */}
      <nav
        className={`vertical-navbar${open ? " vertical-navbar--open" : ""}`}
        onClick={() => open && setOpen(false)}
      >
        <ul
          className="vertical-navbar__menu"
          onClick={e => e.stopPropagation()}
        >
          {/* MNIT Logo absolutely at the top of the navbar */}
          <div style={{
            position: 'absolute',
            top: 18,
            left: 0,
            right: 0,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 101,
          }}>
            <a href="https://mnit.ac.in/" target="_blank" rel="noopener noreferrer" className="vertical-navbar__link" tabIndex={0} style={{ padding: 0, background: 'none' }}>
              <img src="/mnit.png" alt="MNIT Logo" style={{ width: 32, height: 32, objectFit: 'contain', borderRadius: 6, background: '#fff' }} />
              <span className="vertical-navbar__tooltip">MNIT Jaipur</span>
            </a>
          </div>
          {navItems.map((item) => (
            <li className="vertical-navbar__item" key={item.label}>
              {item.to !== "#" ? (
                <Link to={item.to} className="vertical-navbar__link" tabIndex={0} onClick={handleNavClick}>
                  {item.icon}
                  <span className="vertical-navbar__tooltip">{item.label}</span>
                </Link>
              ) : (
                <span className="vertical-navbar__link" tabIndex={0}>
                  {item.icon}
                  <span className="vertical-navbar__tooltip">{item.label}</span>
                </span>
              )}
            </li>
          ))}
        </ul>
      </nav>
      {/* Overlay background for open menu */}
      {open && <div className="vertical-navbar__overlay" onClick={() => setOpen(false)}></div>}
    </>
  );
} 