import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import PropertyCard from "./PropertyCard";
import "./css/HomePage.css";
import Header from "./Header";
import Footer from "./Footer";
import HousePriceChart from "../components/HousePriceChart";
import axios from "axios";
import PropertyCardCarousel from "../components/PropertyCardCarousel";

const HomePage = () => {
  const [housePriceGraphData, setHousePriceGraphData] = useState({
    years: [],
    states: [
      {
        state: "Select State",
        prices: [],
      },
    ],
  });
  const [selectedState, setSelectedState] = useState(
    housePriceGraphData.states[0].state
  );

  const [featuredProperties, setFeaturedProperties] = useState([]);

  const handleStateChange = (event) => {
    setSelectedState(event.target.value);
  };

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5001/api/properties")
      .then((response) => {
        // Slice the response data to get only the first 5 properties
        const firstFiveProperties = response.data.slice(0, 5);
        setFeaturedProperties(firstFiveProperties);
      })
      .catch((error) => console.error("Error fetching properties:", error));
  }, []);

  useEffect(() => {
    axios
      .get("./house-price-graph.json")
      .then((response) => {
        setHousePriceGraphData(response.data);
      })
      .catch((error) => console.error(error));
  }, []);

  useEffect(() => {
    if (housePriceGraphData.years.length !== 0)
      setSelectedState(housePriceGraphData.states[1].state);
  }, [housePriceGraphData]);

  const filteredData = housePriceGraphData.states.find(
    (stateData) => stateData.state === selectedState
  );

  const featuredPropertyCards = featuredProperties.map((property) => (
    <PropertyCard property={property} key={property.HomeId} />
  ));

  return (
    <React.Fragment>
      <Header />
      <div className="hero-section">
        <div className="hero-section-left">
          <div className="hero-section-left-content-wrapper">
            <h2>Welcome to DreamNest</h2>
            <p>Your dream home awaits</p>
            <Link to="/properties" className="cta-button">
              Browse Listings
            </Link>
          </div>
        </div>
        <div className="hero-section-right">
          <img
            className="hero-section-image"
            src="./assets/banner-image.jpg"
            alt="Banner"
          />
        </div>
      </div>
      <div className="house-price-graph-feature-section">
        <div className="house-price-graph-feature-section-left">
          <HousePriceChart
            filteredData={filteredData}
            years={housePriceGraphData.years}
          />
        </div>
        <div className="house-price-graph-feature-section-right">
          <h2>Track the Evolution of House Prices Across the U.S.</h2>
          <p>
            Explore how house prices have changed over the years in different
            states. Use the dropdown menu to select a state and view detailed
            trends. Stay informed with our comprehensive analysis of the real
            estate market
          </p>
          <div className="state-filter">
            <select
              id="state-select"
              value={selectedState}
              onChange={handleStateChange}
            >
              {housePriceGraphData.states.map((stateData) => (
                <option key={stateData.state} value={stateData.state}>
                  {stateData.state}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>
      <div className="featured-properties-card-carousel-section">
        <div className="featured-properties-card-carousel-section-top">
          <h2>Featured Properties</h2>
        </div>
        <div className="featured-properties-card-carousel-section-cards">
          <PropertyCardCarousel propertyCards={featuredPropertyCards} />
        </div>
      </div>
      <Footer />
    </React.Fragment>
  );
};

export default HomePage;
