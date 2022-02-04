import React, {useState, useEffect} from 'react'
import { Link } from 'react-router-dom'
import BackgroundImage from '../assets/blackatlas.jpg'
import Sidebar from './Sidebar'
import Audittable from './Audittable'
import Dataplot from './Dataplot'
import { Card } from 'react-bootstrap';
import '../Homepage.css'

import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { states } from "../data/states";
import { radardata } from "../data/radars";
import DateTimePicker from 'react-datetime-picker';
import { dateconv } from '../helpers/date';
import { getData} from '../api/image';
import { useAuth } from "../context/GlobalContext";

const weatherType = ['reflectivity', 'velocity', 'spectrum_width']

function Ecard(){
    return (<Card style={{ width: '18rem' , marginLeft: '30vh', marginTop: '0vh'}}>
    <Card.Body>
      <Card.Title>Card Title</Card.Title>
      <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
      <Card.Text>
        Some quick example text to build on the card title and make up the bulk of
        the card's content.
      </Card.Text>
      <Card.Link href="#">Card Link</Card.Link>
      <Card.Link href="#">Another Link</Card.Link>
    </Card.Body>
  </Card>);
}




function BigCard({setBody, openModal, body, setLoading, setData}){

  
	const [dist, setDist] = useState([]);
  const [dvalue, onDChange] = useState(new Date());
  const { state } = useAuth();

  function handleData({ target }) {
		setBody((prev) => ({ ...prev, [target.name]: target.value }));
	}

  
  async function handleSubmit(e){
    e.preventDefault();
    openModal();

    var result = await getData(body, state.user);
    if (result.success === true) {
      setLoading(false);
      setData(result.data);
    } 

    else{
      alert('Querry Failed!');
      openModal();
    }
  }

  useEffect(() => {
    
    setBody((prev) => ({ ...prev, timestamp: dateconv(dvalue) }));

	}, [dvalue]);

	useEffect(() => {
		if (body.state) {
			setDist(radardata[body.state]);
		}
	}, [body.state]);
  
    return (<Card className="bigcard">
    <Card.Body>
      <Card.Title>Querry Generator</Card.Title>
      <Card.Subtitle className="mb-2 text-muted">Enter Details and Submit Querry</Card.Subtitle>
      <Form style={formStyle} onSubmit={handleSubmit} >
      <div style={{display:'flex', textAlign:'center'}}>

      <Form.Group controlId="formGridState">
							<Form.Label className="label">State :</Form.Label>
							<Form.Control
								className="input"
								name="state"
								as="select"
								onChange={handleData}
								required
							>
								<option value="">Select State</option>
								{states.map((value) => (
									<option value={value.state_name}> {value.state_name} </option>
								))}
							</Form.Control>
						</Form.Group>
      
      <Form.Group controlId="station">
							<Form.Label className="label">Radar :</Form.Label>
							<Form.Control
								className="input"
								name="station"
								as="select"
								onChange={handleData}
								required
							>
								<option value="">Select Radar</option>
								{dist.map((value, index) => (
									<option key={index} value={value[1]}>
										{" "}
										{value[0]}{" "}
									</option>
								))}
							</Form.Control>
						</Form.Group>

            <Form.Group controlId="visualize">
							<Form.Label className="label">Type :</Form.Label>
							<Form.Control
								className="input"
								name="visualize"
								as="select"
								onChange={handleData}
								required
							>
								<option value="">Select Type</option>
								{weatherType.map((value, index) => (
									<option key={index} value={value}>
										{" "}
										{value}{" "}
									</option>
								))}
							</Form.Control>
						</Form.Group>
  
      </div>
      {/* <Card.Text>
        Some quick example text to build on the card title and make up the bulk of
        the card's content.
      </Card.Text> */}
      <DateTimePicker
        className="datetime"
        key="timestamp"
        onChange={onDChange}
        value={dvalue}
        clearIcon={null}
        
      />
      <Button
								className="button"
								variant="primary"
								type="submit"
                onSubmit={handleSubmit}
							>
								SUBMIT
							</Button>

      </Form>
    </Card.Body>
  </Card>);

}


export default function HomePage() {
    const [showModal, setShowModal] = useState(false);
    const [body, setBody] = useState({});
    const [data,setData] = useState("");
    const [loading, setLoading] = useState(true);
   
    
    


    const openModal = () => {
      setShowModal(prev => !prev);
    }

    return (
        
        <div style={HeaderStyle}>
            <Sidebar  />
            <Dataplot data={data} loading={loading} body={body} showModal={showModal} openModal={openModal} setLoading={setLoading} setData={setData}/>
            <div style={{display:"flex"}}>
            <Ecard />
            <Ecard />
            <Ecard />
            </div>
            <div style={{display:"flex"}}>
            <Audittable showModal={showModal} openModal={openModal} setLoading={setLoading} setData={setData}/>
            <BigCard  setData={setData} setBody={setBody} body={body} setLoading={setLoading} openModal={openModal}  /></div>
        </div>
    )
}

const HeaderStyle = {
    width: "100%",
    height: "100vh",
    background: `url(${BackgroundImage})`,
    backgroundPosition: "center",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover"
}

const formStyle = {display:'flex',  alignItems: 'center', flexDirection: 'column'}