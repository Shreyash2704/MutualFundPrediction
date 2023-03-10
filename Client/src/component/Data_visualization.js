
import React from "react";
import Chart from "chart.js/auto";
import { Line } from "react-chartjs-2";



const Data_visualization = (props) => {
  const labels = props.X
  console.log(props.y)
const data = {
  labels: labels,
  datasets: [
    {
      label: props.title,
      backgroundColor: "rgb(255, 99, 132)",
      borderColor: "rgb(255, 99, 132)",
      data: props.y,
    },
  ],
};
  return (
    <div style={{width:props.width}}>
      <Line data={data}/>
      
    </div>
  );
};

export default Data_visualization;