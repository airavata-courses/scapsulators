require('dotenv').config(); 
const axios = require("axios");
var querystring = require('querystring');
const {generateHash, compareHash} = require('../helpers/encrypt');

const authUrl = process.env.AUTH_URL;
//const authUrl = "http://localhost:8081/"

module.exports = {

// get request check password

login: async (req, res, next) => {

    try{
   
       await axios.post(authUrl + 'login/authenticate',
        querystring.stringify({
                username: req.body.username, //gave the values directly for testing
                password: 'dfasdfdasf'
        }), {
          headers: { 
            "Content-Type": "application/x-www-form-urlencoded"
          }
        }).then((result) => {

        if(result.data.status == "200") {
            const pass = result.data.message;
            console.log(pass);
            if (compareHash(req.body.password, pass)) {
                res.status(200);
            res.json({message: "Signin Succesful", status: 200});

            }

            else {
                res.status(200);
            res.json({message: "Invalid Credentials", status: 500});
            }

            
        }

        else {
            res.status(200);
            res.json({message: "Invalid Credentials", status: 500});
        } }
    ).catch((err)=>{
        res.status(500);
        res.json({error:err.toString(), status: 500});});
 
    }
    
    catch(err){
        
        res.json({error:err.toString(), status: 500})
    }
    
},


//post new user

register: async (req, res, next) => {

    try{
        const hash = generateHash(req.body.password)
        
        await axios.post(authUrl + 'login/signup',
        querystring.stringify({
            username: req.body.username,
            password: hash,
            firstName: req.body.firstName,
            lastName: req.body.lastName,
            secQtAns: req.body.secQtAns,
            city: req.body.city,
            state: req.body.state,
            emailAdd: req.body.emailAdd,
        }), {
          headers: { 
            "Content-Type": "application/x-www-form-urlencoded"
          }
        }).then((result) =>{
            if(result.data.status == "200") {
                res.status(200);
                res.json({message: "Signup Succesful", status: 200});
            }

            else if(result.data.status == "201") {
                res.status(200);
                res.json({message: "User Already exists", status: 201});
            }

            else{
                res.status(500);
                res.json({message: "Server Error", status: 500});
            }
        
        }).catch((err)=>{
            res.json({error:err.toString(), status: 500})});
        
    }
    
    catch(err){
        
        res.json({error:err.toString(), status: 500})
    }
    


},


// post forgot password

forgot: async (req, res, next) => {
    /* calls 2 microservices in the backend forgot to check correct security answer and update to update the password. */
    
    try{
        
        await axios.post(authUrl + 'login/forgotpassword',
        querystring.stringify({
            "username": `${req.body.username}`,
            "secQtAns": `${req.body.secQtAns}`,   
        }), {
          headers: { 
            "Content-Type": "application/x-www-form-urlencoded"
          }
        }).then((result) => {

            if (result.data.status == "200") {
                res.status(200);
                res.json({message: "Security Answer is correct", status: 200});
            }

            else if (result.data.status == "202") {
                res.status(200);
                res.json({message: "User doesn't exist", status: 202});
            }

            else if (result.data.status == "405") {
                res.status(200);
                res.json({message: "Security Answer is incorrect", status: 202});
            }

            else {
                res.status(500);
                res.json({message: "Server Error", status: 500});
            }

            }).catch((err) => {
                res.json({error:err.toString(), status: 500});
            })
  

    }
    
    catch(err){
        res.json({error:err.toString(), status: 500});
    }

},

updatepass: async (req, res, next) => {

    try{
        await axios.post(authUrl + 'login/updatepassword',
                                querystring.stringify({
                                    "username": `${req.body.username}`,
                                    "password": `${generateHash(req.body.password)}`
                                }), {
                                  headers: { 
                                    "Content-Type": "application/x-www-form-urlencoded"
                                  }
                                }).then((result)=> {

                                    if (result.data.status == "200") {
                                        res.status(200);
                                        res.json({message: "Security Answer is correct", status: 200});
                                    }
                        
                        
                                    else {
                                        res.status(500);
                                        res.json({message: "Server Error", status: 500});
                                    }
                                })
    }
    catch(err){
        res.json({error:err.toString(), status: 500});
    }
}
}

