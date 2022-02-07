import React, {useState} from 'react'
import { Link } from 'react-router-dom'
import BackgroundImage from '../assets/earth.jpg'
import axios from "axios";
import { useNavigate  } from "react-router-dom";
import '../App.css'

export default function SignUpPage() {

    const [body, setBody] = useState({});
    const navigate = useNavigate();

    function handleData({ target }) {
		setBody((prev) => ({ ...prev, [target.name]: target.value }));
	}

    function handleSubmit(e){
        e.preventDefault();
        console.log(body);
        axios.post("http://localhost:5000/api/register", body)
            .then((res) => {
                if(res.data.status == 200) {
                    alert('Registered Succesfully!');
                    navigate('/');
                }
                    else if (res.data.status == 201) {
                        alert("User already exists!");
                    }
                    else{
                        alert("Something went wrong!");
                    }
                
            })
            .catch((error) => {
              alert("Something Went Wrong!");
            });
      }

    
    return (
        <div style={HeaderStyle}  >
            <div className="center-object">
            <div className='container-block'>
            <h2>Sign Up!</h2>
            <h5>Create your account</h5>
            </div>
            <form onSubmit={handleSubmit}>
                <p>
                    <label>Username</label><br/>
                    <input type="text" name="username"  onChange={handleData} required />
                </p>
                <p>
                    <label>Email address</label><br/>
                    <input type="email" name="emailAdd" onChange={handleData} required />
                </p>
                <p>
                    <label>Password</label><br/>
                    <input type="password" name="password" onChange={handleData} required />
                </p>
                <p>
                    <label>First Name</label><br/>
                    <input type="text" name="firstName" onChange={handleData} required />
                </p>
                <p>
                    <label>Last Name</label><br/>
                    <input type="text" name="lastName" onChange={handleData} required />
                </p>
                <p>
                    <label>City</label><br/>
                    <input type="text" name="city" onChange={handleData} required />
                </p>
                <p>
                    <label>State</label><br/>
                    <input type="text" name="state" onChange={handleData} required />
                </p>
                <p>
                    <label>What is your mother's maiden name?</label><br/>
                    <input type="text" name="secQtAns" onChange={handleData} required />
                </p>
                <p>
                    <input type="checkbox" name="checkbox" id="checkbox" required /> <span>I agree all statements in <a href="https://google.com" target="_blank" rel="noopener noreferrer">terms of service</a></span>.
                </p>
                <p>
                    <button id="sub_btn" type="submit">Register</button>
                </p>
                <p><Link to="/">Back to Homepage</Link>.</p>
            </form>
            <footer>
                
            </footer>
            </div>
        </div>
    )

}

const HeaderStyle = {
    width: "100%",
    height: "100vh",
    background: `url(${BackgroundImage})`,
    backgroundPosition: "center",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover",
    textAlign:"center",
    
}