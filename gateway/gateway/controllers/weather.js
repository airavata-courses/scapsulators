const axios = require("axios");

const weathUrl = "http://localhost:8081/"

module.exports = {

    getImg: async (req, res, next) => {
        try{

            axios.get(weathUrl + 'getimg', res.body).then((result) => {
                res.status(200);
                res.json({data: result.data, status: 200});
            })
        }
        catch(err){
            res.json({error:err.toString(), status: 500});   
        }

    }}