import {useEffect,useState} from 'react'
import './App.css';
import { Form } from 'react-bootstrap';
import Data_visualization from './component/Data_visualization';
import {BrowserRouter as Router,Route,Link, Routes,Navigate, useNavigate} from 'react-router-dom'
import PastPerformance from './component/PastPerformance';
import Homepage from './component/Homepage';
import BestMutualFund from './component/BestMutualFund';
import FuturePredVisualization from './component/FuturePredVisualization';
import axios from 'axios';

function App() {

  const config = {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET"
    }
  };

  const loadData = async() =>{
    const uri = 'http://localhost:8080/fundname'
    const data = await axios.get(uri,config)
    console.log(data)
  }
  useEffect(() => {
   //loadData()
  }, [])
  
  return (
    <div className="">
      <Router>
      <Routes>
        <Route exact path="/" element={<Homepage />}/>
        <Route exact path="/mutual_fund_past_performance" element={<PastPerformance/>}></Route>
        <Route exact path="/bestMutualFund" element={<BestMutualFund/>}></Route>
        <Route exact path="/futureTimeline" element={<FuturePredVisualization />}></Route>
      </Routes>
      </Router>
    </div>
  );
}

export default App;
