// src/pages/PropertyDetailPage.js
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import "./css/PropertyDetailPage.css";

const PropertyDetailPage = () => {
  const { id } = useParams();
  const [property, setProperty] = useState(null);
  
  useEffect(() => {
    axios
      .get('http://127.0.0.1:5001/api/properties')
      .then((response) => {
        const property = response.data.find(p => p.HomeId == id); // Use == for loose comparison
        setProperty(property);
      })
      .catch((error) => console.error(error));
  }, [id]);

  if (!property) return <div>Loading...</div>;

  return (
    <div className="property-detail-page">
      <h1>{property.Street}</h1>
      {/* Uncomment and use the actual property fields as needed */}
      {/* <img
        src={property.image}
        alt={property.title}
        className="property-detail-image"
      /> */}
      {/* <p>{property.description}</p> */}
      <p>Price: {property.Price}</p>
      <p>Location: {property.City}, {property.State}</p>
      <p>Bed: {property.Beds}</p>
      <p>Bath: {property.Bath}</p>
      <p>Area: {property.Area}</p>
    </div>
  );
};

export default PropertyDetailPage;
