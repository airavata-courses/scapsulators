import React from 'react';
import {
    BrowserRouter as Router,
    Route,
    Routes,
  } from "react-router-dom";
  import LandingPage from '../components/LandingPage'
  import LoginPage from '../components/LoginPage'
  import RegisterPage from '../components/RegisterPage'
  import ForgetPasswordPage from '../components/ForgetPasswordPage'
  import HomePage from '../components/HomePage'
  import { useAuth } from "../context/GlobalContext"

function Index() {
    const { state } = useAuth();
  if(state.user) {
  return <Router>
  <div>
      
      <Routes>
          <Route exact path="/" element={<LandingPage/>}/>
          <Route path="/login" element={<LoginPage/>} />
          <Route path="/register" element={<RegisterPage/>} />
          <Route path="/forget-password" element={<ForgetPasswordPage/>} />
          <Route path="/home" element={<HomePage/>} />
          <Route path='*' element={<LandingPage/>}/>
      </Routes>
      <Footer />
  </div>
</Router> ;}

else {
   return  <Router>
   <div>
       
       <Routes>
           <Route exact path="/" element={<LandingPage/>}/>
           <Route path="/register" element={<RegisterPage/>} />
           <Route path="/forget-password" element={<ForgetPasswordPage/>} />
           <Route path="/test" element={<HomePage/>} />
           <Route  path='*' element={<LandingPage/>}/>
       </Routes>
       <Footer />
   </div>
 </Router>

}
}

const Footer = () => {
    return (
        <p className="text-center" style={ FooterStyle }>Team <a href="https://github.com/airavata-courses/scapsulators" target="_blank" rel="noopener noreferrer">Scapsulators</a></p>
    )
}

const FooterStyle = {
    background: "#222",
    fontSize: ".8rem",
    color: "#fff",
    position: "fixed",
    bottom: 0,
    padding: "1rem",
    margin: 0,
    width: "100%",
    opacity: "0.7"
}

export default Index;
