import React,{useState,useEffect} from 'react'
import { Button, Form } from 'react-bootstrap'
import Data_visualization from './Data_visualization'
import axios from 'axios'

export default function FuturePredVisualization() {

  const [show, setshow] = useState(false)
  const [fundno, setfundno] = useState(0)
  const [duration, setduration] = useState(0)
  const [X, setX] = useState([])
  const [y, sety] = useState([])
  const [fundname, setfundname] = useState("")

  const getData = async(fundno,duration) =>{
    if(fundno != 0 && duration !=0){
      const data = {
        modelno:fundno,
        duration:duration
      }

      console.log(data)
      const uri = "http://localhost:8080/future_nav"
      const get_data = await axios.post(uri,data)
      console.log(get_data.data)
      setX(get_data.data.Date)
      sety(get_data.data.Nav)
      setshow(true)
      setfundname(get_data.data.fund_name)
    }
  }

  const handleSelect = (e) =>{
    const {name,value} = e.target
    setfundno(value)
  }
  const handleDuration = (e) =>{
    const {name,value} = e.target
    setduration(value)
  }
  return (
    <div>
        <div className='mx-5'>
            <a href="/" class="btn btn-success mt-3">Go Back</a>
            <Form className='row'>
            <div className='col-4 mt-2'>
            <Form.Select aria-label="Default select example" onChange={(e)=>setfundno(e.target.value)}>
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
            <div className='col-4 mt-2'>
              <Form.Control type="number" name="duration" max="12" min="0" placeholder='duration' onChange={(e)=>setduration(e.target.value)}></Form.Control>
            </div>

            <div className='col-4 mt-2'>
              <Button onClick={()=>getData(fundno,duration)}>Apply</Button>
            </div>
            </Form>
        </div>
       
        {show && <div className='d-flex justify-content-center align-items-center bg-light m-5'>
            <Data_visualization width="1200px" X={X} y={y} title={fundname}/>
        </div>}
    </div>
  )
}
