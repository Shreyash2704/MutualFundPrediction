import React from 'react'
import { Form } from 'react-bootstrap'
import BestMutualFund from './BestMutualFund'
import Data_visualization from './Data_visualization'
import NavPrediction from './NavPrediction'

export default function Homepage() {
  return (
    <div className='container-fluid'>
    <div className=' m-3 bg-light p-5'>
      <h3>Future fund predition and recommendation for following mutual funds</h3>
      <ul>
        <li>SBI consumption opportunities fund <a href="/mutual_fund_past_performance">see past performance</a></li>
        <li>SBI contra fund</li>
        <li>SBI Equity Hybrid Fund</li>
        <li>SBI focused fund</li>
        <li>SBI healthcare opportunities fund</li>
        <li>SBI Large & Midcap Fund</li>
        <li>SBI Magnum Equity ESG Fund</li>
        <li>SBI Magnum Income Fund</li>
        <li>SBI Nifty Index Fund</li>
        <li>SBI small cap</li>
      </ul>

     
      <p><a href="/bestMutualFund">Mutual Fund Recommendation to invest</a></p>
      <p><a href="/futureTimeline">Future timeline predition</a></p>
      
      
      </div>
      
      <NavPrediction />
      
    </div>

  )
}
