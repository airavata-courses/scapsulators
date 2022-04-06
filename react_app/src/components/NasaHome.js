import React, {useState} from 'react';
import ReactTooltip from "react-tooltip";
import GeoPlot from "./GeoPlot";
import '../Homepage.css';
import BackgroundImage from '../assets/blackatlas.jpg';
import Sidebar from './Sidebar';
import DatePicker from 'react-date-picker';
import newData from '../data/temp.json';
import { useEffect } from 'react';
import Button from "react-bootstrap/Button";
import {getNasaData} from "../api/getnasa";


function NasaHome() {
    const [content, setContent] = useState("");
    const [value, onChange] = useState(new Date());
    const [time, setTime] = useState(0);
    const [dataset, setDataset] = useState(newData);
    const [data, setData] = useState(newData["0"]);
    const [nasaType, setNasaType] = useState("ALBEDO");

    
    async function handleSubmit(e){ 
      console.log(value.toLocaleDateString());
      //hit gateway api
      //and set dataset and data it will work
      console.log({id: -1, visualize: nasaType, timestamp: value.toLocaleDateString('zh-Hans-CN',  { year: 'numeric', month: '2-digit', day: '2-digit' }).replaceAll('/','-') });
      let res = await getNasaData({id: -1, visualize: nasaType, timestamp: value.toLocaleDateString('zh-Hans-CN',  { year: 'numeric', month: '2-digit', day: '2-digit' }).replaceAll('/','-') });
      if (res.success) {
      console.log(res.data);
      setDataset(res.data);
      setData(res.data[time.toString()]);}
      else {
        alert('Failed!');
      }

    }

    const handleCategoryChange = (val) => {

      setNasaType(val);


    } 
    
    
    return (
      <div style={HeaderStyle}>
          <Sidebar  />
          
          <h1 style={{display:'flex', flexDirection:'column', alignItems:'center'}}>MERRA DATA <p style={{color:'orange',fontSize:'3vh' ,background:'black', width:'fit-content'}}>{value.toDateString().slice(3)}</p>
          <p style={{background:'black', width:'fit-content', fontSize:'1.5vh'}}>Change Time Step</p>
          </h1>
          
          <input
          type="range"
          min={0}
          max={5}
          step={1}
          onChange={event => {
            setTime(event.target.valueAsNumber);
            setData(dataset[time.toString()]);
          }}
        />
        <GeoPlot setTooltipContent={setContent} data={data} />
        <ReactTooltip>{content}</ReactTooltip>
        <div style={{display:"flex", flexDirection:"column", alignItems:"center"}}>
        <select style={{marginBottom:'2vh'}} name="category"  onChange={event => handleCategoryChange(event.target.value)}>
            <option id="0" value='ALBEDO' >ALBEDO </option>
            <option id="1" value='LWGNTICE'>LWGNTICE</option>
        </select>
								
            <DatePicker className="date" onChange={onChange} value={value} isOpen={true} clearIcon={null}/>
            <Button
								className="button"
                style={{width:"10%"}}
								variant="primary"
								type="submit"
                onClick={handleSubmit}
							>
								Visualize
							</Button>
              </div>
      </div>
    );
}

const HeaderStyle = {
    width: "100%",
    height: "100vh",
    background: `url(${BackgroundImage})`,
    backgroundPosition: "center",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover",
    color: 'white',
    textAlign: 'center',
    alignItems: 'center'
}


export default NasaHome
