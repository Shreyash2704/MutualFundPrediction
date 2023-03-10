
import React from "react";
import Chart from "chart.js/auto";
import { Line } from "react-chartjs-2";



const Data_visualization = (props) => {
  const labels = props.labels
  const all_data = props.all_data
  const fundname= props.fundnames
  const color = ["red","blue","green","grey","black","violet","darkgreen","purple","yellow","darkred"]
  
  console.log(fundname)
  var dataset_arr = []
  var count = 0
  all_data.map((ele)=>{
    const ele_data = {
        label: fundname[count],
        backgroundColor: color[count],
        borderColor: color[count],
        data: ele
    }
    dataset_arr.push(ele_data)
    count = count +1
  })

  
const data = {
  labels: labels,
  datasets: dataset_arr
};
  return (
    <div style={{width:props.width}}>
      <Line data={data}/>
      
    </div>
  );
};

export default Data_visualization;