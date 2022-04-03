const axios = require("axios");
require('dotenv').config(); 
var querystring = require('querystring');
var qs = require('qs');
const { OAuth2Client } = require('google-auth-library')



const sessUrl = process.env.sessUrl;
const client = new OAuth2Client(process.env.CLIENT_ID)

module.exports = {


    verify: async (req,res,next) => {

        try{
        
        const ticket = await client.verifyIdToken({ 
                                                    idToken: req.body.token,
                                                    audience: process.env.CLIENT_ID
                                                });

        console.log(ticket);
        res.json({message: "Token valid!", user: ticket['payload']['name'] , status: 200});
        }
        catch(err){
            res.json({error:err.toString(), status: 500});
        }

        
    },



}