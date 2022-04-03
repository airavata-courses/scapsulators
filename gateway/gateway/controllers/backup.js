const axios = require("axios");
require('dotenv').config(); 
var querystring = require('querystring');
var qs = require('qs');


const sessUrl = process.env.sessUrl;


module.exports = {

    create: async (req,res,next) => {
        
        try{
                var data = querystring.stringify({
                    "token": `${req.body.token}`,
                    "mailAdd": `${req.body.mailAdd}`
                });
                
                var config = {
                method: 'get',
                url: sessUrl + 'session/createSession',
                headers: { 
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data : data
                };
            console.log(data);
            await axios(config).then((result)=> {

                                    console.log(result.data);

                                    if (result.data.status == "200") {
                                        res.status(200);
                                        res.json({message: "Token saved!", status: 200});
                                    }
                        
                        
                                    else {
                                        res.status(500);
                                        res.json({message: "Server Error", status: 500});
                                    }
                                }).catch((err) => {
                                    res.send(err);
                                    //console.log(err);
                                    //res.json({error:err.toString(), status: 500});
                                });


        }
        catch(err){
            res.json({error:err.toString(), status: 500});
        }

    },


    verify: async (req,res,next) => {

        try{
            await axios.post(sessUrl + 'session/verifyToken',
                                querystring.stringify({
                                    "token": `${req.body.token}`,
                                    "mailAdd": `${req.body.mailAdd}`
                                }), {
                                  headers: { 
                                    "Content-Type": "application/x-www-form-urlencoded"
                                  }
                                }).then((result)=> {

                                    if (result.data.status == "200") {
                                        res.status(200);
                                        res.json({message: "Token valid!", status: 200});
                                    }

                                    else if (result.data.status == "400") {
                                        res.status(200);
                                        res.json({message: "Verification Failed!", status: 400});
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



    destroy: async (req,res,next) => {

        try{
            await axios.post(sessUrl + 'session/verifyToken',
                                querystring.stringify({
                                    "token": `${req.body.token}`,
                                    "mailAdd": `${req.body.mailAdd}`
                                }), {
                                  headers: { 
                                    "Content-Type": "application/x-www-form-urlencoded"
                                  }
                                }).then((result)=> {

                                    if (result.data.status == "200") {
                                        res.status(200);
                                        res.json({message: "Token destroyed!", status: 200});
                                    }

                                    else if (result.data.status == "400") {
                                        res.status(200);
                                        res.json({message: "Toker or user does not exist", status: 400});
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

        
        
    }



}