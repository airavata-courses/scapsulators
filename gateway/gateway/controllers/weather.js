const axios = require("axios");

const weathUrl = "http://localhost:5001/"

module.exports = {

    getImg: async (req, res, next) => {
        try{
            
            
            var data = JSON.stringify(req.body);
            console.log(req.body);
            var config = {
            method: 'get',
            url: weathUrl + 'getWeatherReport',
            headers: { 
                'Content-Type': 'application/json'
            },
            responseType: 'arraybuffer',
            data : data
            };

            axios(config)
            .then(function (response) {
                
                
                res.send(response.data.toString('base64'));

            })
            .catch(function (error) {
                res.status(500);
                res.json({ data: error, status: 500});
            });

        }
        catch(err){
            res.status(500);
            res.json({error:err.toString(), status: 500});   
        }

    }}