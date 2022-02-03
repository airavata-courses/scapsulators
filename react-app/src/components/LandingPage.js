import React from 'react'
import { Link } from 'react-router-dom'

import '../App.css'
import BackgroundImage from '../assets/img-home.jpg'
import BackgroundVideo from '../assets/video-2.mp4'
import LoginPage from './LoginPage'


export default function LandingPage() {

    return (
        <header style={HeaderStyle} >
            
        <video style={backgroundVid} autoPlay loop muted >
        <source src={BackgroundVideo} type="video/mp4" />
        </video>
            
            <h1 className="main-title text-center"><span className="main-titlespan">RefleXor</span></h1>
            <p className="main-para text-center"></p>
            <div className='container-home'>
            <LoginPage />
            </div>
            {/*
            <div className="buttons text-center">
                <Link to="/login">
                    <button className="primary-button">log in</button>
                </Link>
                <Link to="/register">
                    <button className="primary-button" id="reg_btn"><span>register </span></button>
                </Link>
            </div> */}
        </header>
    )
}

const HeaderStyle = {
    alignItems: 'center',
    display: 'flex',
    flexDirection: 'column',
  
}

const backgroundVid = {
    width: "100vw",
    height: "100vh",
    objectFit: "cover",
    position: "fixed",
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    zIndex: -1,

}

