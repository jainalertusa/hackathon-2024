// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import './css/Header.css';

const Header = () => (
  <header className="header">
    <div className="header-content">
      <div className="logo">
        <Link to="/">DreamNest</Link>
      </div>
      <nav className="navigation">
        <ul>
          <li><Link to="/properties">Properties</Link></li>
        </ul>
      </nav>
    </div>
  </header>
);

export default Header;
