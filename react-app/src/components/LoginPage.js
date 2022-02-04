import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import axios from "axios";
import { useNavigate  } from "react-router-dom";
import { useAuth } from "../context/GlobalContext";
import '../App.css'

export default function SignInPage() {

    const [username, setUname] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    const [error, setError] = useState(null);
    const { state, login } = useAuth();

    const handleLogin = (event) => {
        event.preventDefault();
          axios
            .post("http://localhost:5000/api/login", { username: username, password: password })
            .then((res) => {
                
                if(res.data.status == 200) {
                login({ user: username});
                navigate('/home');}

                else{
                    alert("Invalid Credentials");
                }
              
            })
            .catch((error) => {
                console.log(error);
              alert("Something went wrong!");
            });
      };


    return (
        <div className="text-center m-5-auto">
            <h2>Sign In</h2>
            <form onSubmit={handleLogin} action="/home">
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
            </form>
            <footer>
                <p>First time? <Link to="/register">Create an account</Link>.</p>
                <p><Link to="/">Back to Homepage</Link>.</p>
            </footer>
        </div>
    )
}
