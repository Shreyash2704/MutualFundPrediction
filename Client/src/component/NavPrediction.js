import axios from 'axios'
import React,{useState,useEffect} from 'react'
import { Button, Form } from 'react-bootstrap'

export default function NavPrediction() {

  const [Nav, setNav] = useState(0)
  const [fundno, setfundno] = useState()
  const [date, setdate] = useState("")
  const fundName = [
    "SBI consumption opportunities fund",
    "SBI contra fund",
    "SBI Equity Hybrid Fund","SBI focused fund","SBI healthcare opportunities fund",
    "SBI Large & Midcap Fund","SBI Magnum Equity ESG Fund","SBI Magnum Income Fund","SBI Nifty Index Fund","SBI small cap"
  ]
  const getPredictedNav = async(fundno,date) =>{
    const uri = "http://localhost:8080/getNav"
    console.log(date)
    const day = date.split("-")[2]
    const month = date.split("-")[1]
    const year = date.split("-")[0]
    const data = {
      fundno:fundno,
      day:day,
      month:month,
      year:year

    }
    const getNav = await axios.post(uri,data)
    setNav(getNav.data)

  }
  return (
    <div className='m-3 p-4 bg-light'>
        <h3>Future prediction for Net Asset Value of Mutual Funds</h3><hr></hr>
        
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
            <Form.Control type="date" name='date' onChange={(e)=>setdate(e.target.value)} />
          </div>

          <div className='col-4 mt-2 '>
           <Button variant="success" onClick={()=>getPredictedNav(fundno,date)}>Submit</Button>
          </div>
          </Form>


          {Nav != 0 && <div className='m-2'>
            <h4 className=' bg-white p-3'>Net Asset Value - {fundName[fundno]} ({date}) <br></br> {Nav}</h4>
          </div>}
         
      </div>
  )
}
