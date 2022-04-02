import React, { useEffect,memo } from "react";
import {
  ComposableMap,
  Geographies,
  Geography,
  Sphere,
  Graticule
} from "react-simple-maps";
import geoData from '../data/samplegeo.json';
import { scaleLinear } from "d3-scale";
import newData from '../data/temp.json';

const geoUrl =
  "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

//   const values = Object.values(geoData);
// //Math.max(...values)
//   const colorScale = scaleLinear()
//   .domain([0, 1])
//   .range(["#ffedea", "#ff5233"]);

const MapChart = ({ setTooltipContent, data }) => {

  
  const values = Object.values(data);
    const colorScale = scaleLinear()
  .domain([Math.min(...values), Math.max(...values)])
  .range(["#ffedea", "#ff5233"]);
  
  return (
    <> <div style={plotStyle}>
      <ComposableMap data-tip="" projectionConfig={{ rotate: [-10, 0, 0],scale: 55}}>
      <Sphere stroke="#E4E5E6" strokeWidth={0.5} />
      <Graticule stroke="#E4E5E6" strokeWidth={0.5} />
      <Geographies geography={geoUrl}  >
      {({ geographies }) =>
            geographies.map((geo) => {
              const d = data[geo.properties.ISO_A2];
              return (
                <Geography
                  key={geo.rsmKey}
                  geography={geo}
                  fill={d ? colorScale(d) : "#F5F4F6"}
                  onMouseEnter={() => {
                    setTooltipContent(geo.properties.NAME);
                  }}
                  onMouseLeave={() => {
                    setTooltipContent("");
                  }}
                  style={{
                    hover: {
                      fill: "#F53",
                      outline: "none"
                    },
                    pressed: {
                      fill: "#E42",
                      outline: "none"
                    }
                  }}
                />
             );
            })
          }
      </Geographies>
    </ComposableMap>
    
    </div>
    </>
  );
};

const plotStyle = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  maxHeight: '50vh',
  overflow: 'hidden'
  }
  
export default memo(MapChart);
