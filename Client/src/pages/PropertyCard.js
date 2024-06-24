// src/components/PropertyCard.js
import React from 'react';
import { Link } from 'react-router-dom';
import './css/PropertyCard.css';

const PropertyCard = ({ property }) => (
  <div className="property-card">
    {/* <img src={property.image} alt={property.title} className="property-image" /> */}
    <div className="property-info">
      <h2>{property.Street}</h2>
      <p>{property.Price}</p>
      <p>{property.City}, {property.State}</p>
      <Link to={`/property/${property.HomeId}`} className="details-link">View Details</Link>
    </div>
  </div>
);

export default PropertyCard;
