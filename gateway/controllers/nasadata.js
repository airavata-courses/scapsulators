const axios = require("axios");
require('dotenv').config();


const nasaURL = process.env.NASA_URL;
console.log(nasaURL);

module.exports = {

    getnasaData: async (req, res, next) => {
        try{
            var data = JSON.stringify({id: -1, visualize: req.body.visualize, timestamp: req.body.timestamp});
            console.log(nasaURL + 'caching/save');
            console.log(data);
            var config = {
            method: 'post',
            url: nasaURL + 'caching/save',
            headers: { 
                'Content-Type': 'application/json'
            },
            data : data
            };

            await axios(config)
            .then(function (response) {

                if (response.data == 'FAIL') {
                    res.status(200);
                res.json({data:response.data, status: 500});

                }
                else{
                res.status(200);
                res.json({data:response.data, status: 200});}

            })
            .catch(function (error) {
                console.log(error);
                res.status(200);
                res.json({ data: error, status: 500});
            });

        }
        catch(err){
            res.status(500);
            res.json({error:err.toString(), status: 500});   
        }

    }}
