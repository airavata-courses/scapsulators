const axios = require("axios");
require('dotenv').config()

const {
    writeAudit
  } = require("../controllers/audit");

//const weathUrl = "http://localhost:5001/"
const weathUrl = process.env.PYTHON_URL

console.log(weathUrl);
module.exports = {

    getImg: async (req, res, next) => {
        try{
            
            const usr = req.body.username;
            delete req.body.username;
            console.log(req.body);
            var data = JSON.stringify(req.body);
            
            console.log(data);
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
                const data = { username: usr, date: req.body.timestamp, time: req.body.visualize , nexradstation: req.body.station}
                writeAudit(data);
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