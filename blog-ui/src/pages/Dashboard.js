import React, { useState } from "react";
import EconomicHistory from "../components/EconomicHistory";
import PropertyMarketHistory from "../components/PropertyMarketHistory";
// Import other visualization components as needed

const Dashboard = () => {
  const [selectedViz, setSelectedViz] = useState("economicHistory");

  const renderVisualization = () => {
    switch (selectedViz) {
      case "economicHistory":
        return <EconomicHistory />;
      case "propertyMarketHistory":
        return <PropertyMarketHistory />;
      case "constructionSpendingHistory":
        return <ConstructionSpendHistory />;
      // Add cases for other visualizations
      default:
        return <EconomicHistory />;
    }
  };

  return (
    <div>
      <h1>Dashboard</h1>
      <div>
        <button onClick={() => setSelectedViz("economicHistory")}>
          Economic History
        </button>
        <button onClick={() => setSelectedViz("propertyMarketHistory")}>
          Property Market History
        </button>
        <button onClick={() => setSelectedViz("constructionSpendingHistory")}>
          Construction Spending History
        </button>
      </div>
      <div>{renderVisualization()}</div>
    </div>
  );
};

export default Dashboard;
