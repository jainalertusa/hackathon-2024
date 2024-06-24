import React from "react";
import TableauViz from "./TableauViz";

const ProprtyMarketHistory = () => {
  const src =
    "https://us-east-1.online.tableau.com/t/schwarzemambajre70feb2d59/views/gdp_unemplyment_year/Sheet2?:origin=card_share_link&:embed=y";

  return (
    <div>
      <h2>Property Market History</h2>
      <div className="visualization-container">
        <tableau-viz
          id="tableauViz"
          src={src}
          toolbar="bottom"
          hide-tabs
        ></tableau-viz>
      </div>
    </div>
  );
};
export default ProprtyMarketHistory;
