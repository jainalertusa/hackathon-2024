// src/routes.js
// src/routes.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import PropertyListPage from './pages/PropertyListingPage';
import PropertyDetailPage from './pages/PropertyDetailPage';

const RoutesComponent = () => (
  <Router>
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/properties" element={<PropertyListPage />} />
      <Route path="/property/:id" element={<PropertyDetailPage />} />
    </Routes>
  </Router>
);

export default RoutesComponent;

