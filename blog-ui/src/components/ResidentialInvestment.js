import React from "react";
import TableauViz from "./TableauViz";

const ResidentialInvestment = () => {
  const src =
    "https://us-east-1.online.tableau.com/t/schwarzemambajre70feb2d59/views/yr_cpi/Sheet2?:origin=card_share_link&:embed=y";

  return (
    <div>
      <h2>Residential Investment</h2>
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

export default ResidentialInvestment;
