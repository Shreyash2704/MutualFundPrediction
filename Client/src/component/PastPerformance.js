import axios from 'axios'
import React,{useState,useEffect} from 'react'
import { Form } from 'react-bootstrap'
import Data_visualization from './Data_visualization'

export default function PastPerformance() {

  const [NAV, setNAV] = useState([])
  const [Date, setDate] = useState([])
  const [fundName, setfundName] = useState("")

  const getData = async(data_no) =>{
    const uri = `http://localhost:8080/past_nav?data_no=${data_no}`
    const data = await axios.get(uri)
    setNAV(data.data.Nav)
    setDate(data.data.Date)
    setfundName(data.data.fund_name)
  }
  return (
    <div>
        <div className="mx-5">
        <a href="/" class="btn btn-success mt-3">Go Back</a>
        <Form className='row'>
          <div className='col-4 mt-2'>
          <Form.Select aria-label="Default select example" onChange={(e)=>getData(e.target.value)}>
            <option>Select the fund </option>
            <option value="0">SBI consumption opportunities fund</option>
            <option value="1">SBI contra fund</option>
            <option value="2">SBI Equity Hybrid Fund</option>
            <option value="3">SBI focused fund</option>
            <option value="4">SBI healthcare opportunities fund</option>
            <option value="5">SBI Large & Midcap Fund</option>
            <option value="6">SBI Magnum Equity ESG Fund</option>
            <option value="7">SBI Magnum Income Fund</option>
            <option value="8">SBI Nifty Index Fund</option>
            <option value="9">SBI small cap</option>
        </Form.Select>
        </div>
        </Form>

        </div>
        <div className='d-flex justify-content-center align-items-center bg-light m-5'>
            <Data_visualization width="1200px" X={Date} y={NAV} title={fundName}/>
        </div>
    </div>
  )
}
