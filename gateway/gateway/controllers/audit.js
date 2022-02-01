const axios = require("axios");

const audUrl = "http://localhost:8081/"
var querystring = require('querystring');

module.exports = {

    getAudit: async (req, res, next) => {
        try{

            axios.get(weathUrl + 'getimg', res.body).then((result) => {
                res.status(200);
                res.json({data: result.data, status: 200});
            })
        }
        catch(err){
            res.json({error:err.toString(), status: 500});   
        }

    },

    writeAudit: async (req, res, next) => {
        try{

            axios.get(weathUrl + 'getimg', res.body).then((result) => {
                res.status(200);
                res.json({data: result.data, status: 200});
            })
        }
        catch(err){
            res.json({error:err.toString(), status: 500});   
        }

    },

}