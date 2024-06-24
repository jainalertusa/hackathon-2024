import React, { useState, Suspense } from "react";
// import axios from "axios";
import "./App.css";
// import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// import EconomicHistory from "./components/EconomicHistory";
const EconomicHistory = React.lazy(
  () => import("./components/EconomicHistory"),
);
const PropertyMarketHistory = React.lazy(
  () => import("./components/PropertyMarketHistory"),
);
const ResidentialInvestment = React.lazy(
  () => import("./components/ResidentialInvestment"),
);

const App = () => {
  const [comp, setComp] = useState(null);
  const renderComponent = () => {
    switch (comp) {
      case "EconomicHistory":
        return <EconomicHistory />;
      case "PropertyMarketHistory":
        return <PropertyMarketHistory />;
      case "ResidentialInvestment":
        return <ResidentialInvestment />;
      default:
        return <div>Select a visualization to display.</div>;
    }
  };
  return (
    // <Router>
    //   <Routes>
    //     <Route path="/" component={Dashboard} />
    //     {/* Add other routes as needed */}
    //   </Routes>
    // </Router>
    <div className="dashboard-container">
      <h1>Multi-Family Investment Market Study</h1>
      <div className="dashboard-buttons">
        <button onClick={() => setComp("EconomicHistory")}>
          Economic History
        </button>
        <button onClick={() => setComp("ResidentialInvestment")}>
          Residential Investment History
        </button>
        <button onClick={() => setComp("PropertyMarketHistory")}>
          Property Market History
        </button>
      </div>
      {/* <EconomicHistory /> */}
      <div className="dashboard-content">
        <Suspense fallback={<div>Loading...</div>}>
          {renderComponent()}
        </Suspense>
      </div>
    </div>
  );
};

export default App;
