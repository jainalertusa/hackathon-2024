// src/components/HeroSection.js
import React from 'react';
import '../pages/css/HeroSection.css';
import { Link } from 'react-router-dom';

const HeroSection = () => (
  <section className="hero">
    <div className="hero-content">
      <h1>Welcome to DreamNest</h1>
      <p>Your ultimate destination for finding the perfect home.</p>
      <Link to="/properties" className="cta-button">Browse Listings</Link>
    </div>
  </section>
);

export default HeroSection;
