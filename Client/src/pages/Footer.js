// src/components/Footer.js
import React from 'react';
import './css/Footer.css';

const Footer = () => (
  <footer className="footer">
    <div className="footer-content">
      <p>&copy; 2024 DreamNest. All rights reserved.</p>
      <ul className="footer-links">
        <li><a href="/">Privacy Policy</a></li>
        <li><a href="/">Terms of Service</a></li>
        <li><a href="/">FAQ</a></li>
      </ul>
    </div>
  </footer>
);

export default Footer;
