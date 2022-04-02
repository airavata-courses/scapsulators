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
            <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
                laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
                velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui o
                fficia deserunt mollit anim id est laborum.</p>


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