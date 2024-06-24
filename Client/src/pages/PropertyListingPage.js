// PropertyListingPage.js

import React, { useState, useEffect } from "react";
import "./css/PropertyListingPage.css"; // Import your CSS file for styling
import axios from "axios";
import PropertyCard from "./PropertyCard";
import Header from "./Header";
import Footer from "./Footer";
import { Link } from "react-router-dom";

const PropertyListingPage = () => {
  const [properties, setProperties] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [propertiesPerPage] = useState(8); // Number of properties per page

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5001/api/properties")
      .then((response) => setProperties(response.data))
      .catch((error) => console.error(error));
  }, []);

  // Pagination logic
  const indexOfLastProperty = currentPage * propertiesPerPage;
  const indexOfFirstProperty = indexOfLastProperty - propertiesPerPage;
  const currentProperties = properties.slice(
    indexOfFirstProperty,
    indexOfLastProperty
  );

  // Change page
  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  return (
    <React.Fragment>
      <Header />
      <div className="property-listing">
        <h2 className="property-listing-header">Property Listings</h2>
        <div className="featured-properties">
          {currentProperties.map((property) => (
            <PropertyCard key={property.HomeId} property={property} />
          ))}
        </div>
        {/* Pagination links */}
        <div className="pagination">
          {Array.from(
            { length: Math.ceil(properties.length / propertiesPerPage) },
            (_, index) => (
              <Link
                key={index + 1}
                to="#"
                className={`page-link ${
                  index + 1 === currentPage ? "active" : ""
                }`}
                onClick={() => paginate(index + 1)}
              >
                {index + 1}
              </Link>
            )
          )}
        </div>
      </div>
      <Footer />
    </React.Fragment>
  );
};

export default PropertyListingPage;
