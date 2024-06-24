import React, { useEffect, useRef } from "react";

const TableauViz = ({
  src,
  width = "100%",
  height = "800px",
  toolbar = "bottom",
  hideTabs = true,
}) => {
  const vizRef = useRef(null);

  useEffect(() => {
    const initViz = () => {
      if (vizRef.current) {
        // Clear any existing viz
        if (vizRef.current.viz) {
          vizRef.current.viz.dispose();
        }

        const options = {
          width,
          height,
          hideTabs,
          toolbarPosition: toolbar,
        };

        vizRef.current.viz = new window.tableau.Viz(
          vizRef.current,
          src,
          options,
        );
      }
    };

    initViz();
  }, [src, width, height, toolbar, hideTabs]);

  return <div ref={vizRef}></div>;
};

export default TableauViz;
