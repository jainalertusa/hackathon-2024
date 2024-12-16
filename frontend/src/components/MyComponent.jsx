import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './MyComponent.css';

const ImageCarousel = ({ imgUrls, onImageClick, className = '' }) => {
  const [currentImgIndex, setCurrentImgIndex] = useState(0);
  const urls = imgUrls.split(',');

  const handleNextImg = (e) => {
    e.stopPropagation();
    setCurrentImgIndex((currentImgIndex + 1) % urls.length);
  };

  const handlePrevImg = (e) => {
    e.stopPropagation();
    setCurrentImgIndex((currentImgIndex - 1 + urls.length) % urls.length);
  };

  return (
    <div className={`carousel ${className}`} onClick={(e) => e.stopPropagation()}>
      <button className="carousel-button left" onClick={handlePrevImg}>{"<"}</button>
      <img 
        src={urls[currentImgIndex]} 
        alt={`Property Image ${currentImgIndex + 1}`} 
        className="carousel-image" 
        onClick={onImageClick} 
      />
      <button className="carousel-button right" onClick={handleNextImg}>{">"}</button>
    </div>
  );
};

const MyComponent = () => {
  const [zipcode, setZipcode] = useState('');
  const [properties, setProperties] = useState([]);
  const [selectedApartment, setSelectedApartment] = useState(null);
  const [dialogOpen, setDialogOpen] = useState(false);
  const [currentPage, setCurrentPage] = useState(0);
  const propertiesPerPage = 5;

  const handleZipcodeSearch = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/api/apartments/${zipcode}`);
      setProperties(response.data);
      setCurrentPage(0);
    } catch (error) {
      console.error('Error fetching properties:', error);
    }
  };

  const handleApartmentClick = async (apartmentId) => {
    try {
      const response = await axios.get(`http://localhost:8000/api/apartment/${apartmentId}`);
      setSelectedApartment(response.data);
      setDialogOpen(true);
    } catch (error) {
      console.error(`Error fetching details for apartment ${apartmentId}:`, error);
    }
  };

  const handleDownloadPDF = async (apartmentId) => {
    try {
      const response = await axios.get(`http://localhost:8000/api/apartment/${apartmentId}/pdf`, {
        responseType: 'blob',
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `apartment-${apartmentId}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);
    } catch (error) {
      console.error(`Error downloading PDF for apartment ${apartmentId}:`, error);
    }
  };

  const handleCloseDialog = () => {
    setDialogOpen(false);
  };

  const handleNextPage = () => {
    if (currentPage < Math.ceil(properties.length / propertiesPerPage) - 1) {
      setCurrentPage(currentPage + 1);
    }
  };

  const handlePreviousPage = () => {
    if (currentPage > 0) {
      setCurrentPage(currentPage - 1);
    }
  };

  const startIndex = currentPage * propertiesPerPage;
  const selectedProperties = properties.slice(startIndex, startIndex + propertiesPerPage);

  return (
    <div className="my-component">
      <header className="header">
        <h1 className="logo">Real Estate Finder</h1>
      </header>
      <div className="search-section">
        <input
          type="text"
          value={zipcode}
          onChange={(e) => setZipcode(e.target.value)}
          placeholder="Enter ZIP code"
          className="search-input"
        />
        <button onClick={handleZipcodeSearch} className="search-button">Search</button>
      </div>
      <div className="properties-section">
        {selectedProperties.map((property) => (
          <div key={property.id} className="property-tile">
            <h3 className="property-address">{property.address}</h3>
            <ImageCarousel 
              imgUrls={property.imgUrls} 
              onImageClick={() => handleApartmentClick(property.id)} 
            />
            <div className="property-details">
              <p><strong>Beds:</strong> {property.beds}</p>
              <p><strong>Baths:</strong> {property.baths}</p>
              <p><strong>Price:</strong> ${property.price}</p>
            </div>
          </div>
        ))}
      </div>
      <div className="pagination">
        <button onClick={handlePreviousPage} className="pagination-button" disabled={currentPage === 0}>Previous</button>
        <button onClick={handleNextPage} className="pagination-button" disabled={currentPage >= Math.ceil(properties.length / propertiesPerPage) - 1}>Next</button>
      </div>
      {dialogOpen && selectedApartment && (
        <div className="dialog-overlay" onClick={handleCloseDialog}>
          <div className="dialog" onClick={(e) => e.stopPropagation()}>
            <button className="close-button" onClick={handleCloseDialog}>×</button>
            <h2>{selectedApartment.address}</h2>
            <div className="dialog-details">
              <div className="details-row">
                <p><strong>Beds:</strong> {selectedApartment.beds}</p>
                <p><strong>Baths:</strong> {selectedApartment.baths}</p>
                <p><strong>Price:</strong> ${selectedApartment.price}</p>
                <p><strong>Construction Year:</strong> {selectedApartment.construction}</p>
              </div>
              <div className="details-row">
                <p><strong>Parking:</strong> {selectedApartment.parking}</p>
                <p><strong>HOA Fees:</strong> ${selectedApartment.homeOwnersAssociationFees}</p>
                <p><strong>Sqft:</strong> {selectedApartment.sqft}</p>
                <p><strong>Price per Sqft:</strong> ${selectedApartment.pricePerSqft}</p>
                <p><strong>Tax:</strong> ${selectedApartment.tax} ({selectedApartment.taxYear})</p>
              </div>
            </div>
            <ImageCarousel imgUrls={selectedApartment.imgUrls} className="dialog-carousel" />
            <button onClick={() => handleDownloadPDF(selectedApartment.id)} className="download-button">Download PDF</button>
          </div>
        </div>
      )}
      <footer className="footer">
        <p>© 2024 Real Estate Finder. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default MyComponent;
