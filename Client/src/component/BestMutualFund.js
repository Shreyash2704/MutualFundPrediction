import axios from 'axios'
import React ,{useState} from 'react'
import { Button, Form } from 'react-bootstrap'
import Data_visualization from './Data_visualization_2'

export default function BestMutualFund() {

  const [duration, setduration] = useState(0)
  const [fundname, setfundname] = useState([])
  const [returns, setreturns] = useState([])

  const [labels, setlabels] = useState([])
  const [all_data, setall_data] = useState([])
  const [fundnames, setfundnames] = useState([])

  
   const getBestMF = async() =>{
    const uri = "http://localhost:8080/bestMFMerged"
    const funddata = {
      dur_m:duration
    }
    const data = await axios.post(uri,funddata)
    setfundname(data.data.Fund_name)
    setreturns(data.data.max_ans)
    console.log(data.data.Fund_name)
    get_all_future_nav()
   }

   const get_all_future_nav = async() =>{
    const uri = "http://localhost:8080/all_future_nav"
    const funddata = {
      duration:duration
    }
    const data = await axios.post(uri,funddata)
    console.log(data.data)
    setall_data(data.data.data)
    setfundnames(data.data.fund_name)
    setlabels(data.data.dates)
   }
  return (
    <div className='m-2 container-fluid p-4 bg-light'>
        <a href="/" className="btn btn-success mb-3" >Go Back</a>
        <h3>Want to know the best Mutual Fund to invest for duration of next 3,6,9,12 months?</h3><hr></hr>
        <Form className='row'>
            <div className='col-sm-6'>
                 <Form.Control type="number" min="0" max="12" onChange={(e) => setduration(e.target.value)} placeholder='duration in months (0-12)'></Form.Control>
            </div>
            <div className='col-sm-6'>
                <Button variant="primary" onClick={()=>getBestMF()}>Show result</Button>
            </div>
        </Form>
        <div className='m-2'>
            {fundname.length !== 0 && 
            <>
            <h3>Top Results</h3>
              <h4 className='p-3 bg-white'>{fundname[0]} - {returns[0]}% returns</h4>
              <h4 className='p-3 bg-white'>{fundname[1]} - {returns[1]}% returns</h4>
              <h4 className='p-3 bg-white'>{fundname[2]} - {returns[2]}% returns</h4>
              </>
              }
            <div className='mt-4 p-5 bg-white'>
            <Data_visualization labels = {labels} all_data={all_data} fundnames={fundnames}/>
            </div>
            
        </div>

        
        
    </div>
  )
}
