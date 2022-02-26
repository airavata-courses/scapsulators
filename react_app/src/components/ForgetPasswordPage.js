import React, {useState} from 'react'
import { Link } from 'react-router-dom'
import BackgroundImage from '../assets/earth.jpg'
import axios from "axios";
import { useNavigate  } from "react-router-dom";

import '../App.css'

export default function ForgetPasswordPage() {

    const [body, setBody] = useState({});
    const [resetFlag, setReset] = useState(true);
    const navigate = useNavigate();

    function handleData({ target }) {
		setBody((prev) => ({ ...prev, [target.name]: target.value }));
	}

    async function handleSubmit(e){
        e.preventDefault();
        await axios.post("http://localhost:30002/api/forgot", body)
            .then((res) => {

                if(res.data.status == 200) {
                   
                    setReset(false);
                }
                    else if (res.data.status == 202) {
                        alert("User does not exist");
                    }

                    else if (res.data.status == 405) {
                        alert("Security Answer is wrong");
                    }
                    else{
                        console.log(res.data);
                        alert("Something went wrong!");
                    }
                
                
            })
            .catch((error) => {
                console.log(error);
              alert("Something Went Wrong!");
            });
      }

      async function handleSubmit2(e){
        e.preventDefault();
        await axios.post("http://localhost:5000/api/updatepass", body)
            .then((res) => {

                if(res.data.status == 200) {
                    alert('Password Reset Succesfully!');
                    navigate('/');
                }
                    
                    else{
                        console.log(res.data);
                        alert("Something went wrong!");
                    }
                
                
            })
            .catch((error) => {
                console.log(error);
              alert("Something Went Wrong!");
            });
      }

    if(resetFlag) {
    return (
        <div style={HeaderStyle}>
            <div className="center-object">
            <div className='container-block'>
            <h2>Reset your password</h2>
            <h5>Enter your email address and security answer</h5>
            </div>
            <form onSubmit={handleSubmit}>
                <p>
                    <label id="reset_pass_lbl">Username</label><br/>
                    <input type="text" name="username" onChange={handleData} required />
                </p>

                <p>
                    <label id="reset_pass_qa">What is your Mother's Maiden name? </label><br/>
                    <input type="text" name="secQtAns" onChange={handleData} required />
                </p>

                {/* <p>
                    <label id="reset_pass">New Password </label><br/>
                    <input type="password" name="password" onChange={handleData} required />
                </p> */}

                <p>
                    <button id="sub_btn" type="submit">Verify Answer</button>
                </p>
            </form>
            <footer>
                <p> <Link to="/register"> Create an account</Link>.</p>
                <p><Link to="/">Back to Homepage</Link>.</p>
            </footer>
            </div>
        </div>
    ) }

    else {
        return (<div style={HeaderStyle}>
            <div className="center-object">
            <div className='container-block'>
            <h2>Reset your password</h2>
            <h5>Enter your email address and we will send you a new password</h5>
            </div>
            <form onSubmit={handleSubmit2}>
                <p>
                    <label id="reset_pass_lbl">Username</label><br/>
                    <input type="text" name="username" onChange={handleData} required />
                </p>

                {/* <p>
                    <label id="reset_pass_qa">New Password</label><br/>
                    <input type="password" name="password" onChange={handleData} required />
                </p> */}

                <p>
                    <label id="reset_pass">New Password </label><br/>
                    <input type="password" name="password" onChange={handleData} required />
                </p>

                <p>
                    <button id="sub_btn" type="submit">Reset Password</button>
                </p>
            </form>
            <footer>
                <p> <Link to="/register"> Create an account</Link>.</p>
                <p><Link to="/">Back to Homepage</Link>.</p>
            </footer>
            </div>
        </div>)
    }
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
