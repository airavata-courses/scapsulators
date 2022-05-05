import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import axios from "axios";
import { useNavigate  } from "react-router-dom";
import { useAuth } from "../context/GlobalContext";
import { url } from '../config';
import '../App.css';
import { GoogleLogin } from 'react-google-login';
import { setCookie, getCookie } from '../services/cookies';

 


export default function SignInPage() {

    const [username, setUname] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    const [error, setError] = useState(null);
    const { state, login } = useAuth();
   

      const responseGoogle = async (response) => {
        //save token api
        console.log(response['tokenId']);
        setCookie(response['tokenId'] , response['profileObj']);
        login({ user: response['profileObj']['email']});
        navigate('/nasa');
        window.location.reload();
      }

      const failedGoogle = async () => {
          alert('login failed');
      }
      
    return (
        <div className="text-center m-5-auto">
            <h2>Sign In</h2>
            <h4> Welcome to our humble abode, fellow weather enthusiasts!!!</h4>


            <GoogleLogin
    clientId="755512768627-2e90n47po82jasu7mqn63m91r8vgeiga.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={responseGoogle}
    onFailure={failedGoogle}
    cookiePolicy={'single_host_origin'}
  />
            {/* <form onSubmit={handleLogin} action="/home">
                <p>
                    <label style={{color:'black'}}>Username</label><br/>
                    <input type="text" name="username" value={username} onChange={(e) => setUname(e.target.value)} required />
                </p>
                <p>
                    <label style={{color:'black'}}>Password</label>
                    <Link to="/forget-password"><label className="right-label">Forget Password?</label></Link>
                    <br/>
                    <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                </p>
                <p>
                    <button id="sub_btn" type="submit">Login</button>
    
                </p>
            </form> */}
            <footer>
                {/* <p>First time? <Link to="/register">Create an account</Link>.</p> */}
                {/* <p><Link to="/">Back to Homepage</Link>.</p> */}
            </footer>
        </div>
    )
}


const customStyle = {
    color: 'orange'
}
