const axios = require("axios");
require('dotenv').config(); 
//const audUrl = "http://localhost:8084/"
const audUrl = process.env.AUDIT_URL;

console.log(audUrl);
module.exports = {

    getAudit: async (req, res, next) => {
        try{

            axios.get(audUrl + 'audit/fetch', { params: { username: req.body.username } }).then((result) => {
                res.status(200);

                result.data.auditDetLst.map( (element,index) => {
                    delete element.currentDate;
                    
                    element['index'] = index + 1;
                    element['Link'] = 'Click Here!';
                    element['Visualization'] = element.time;
                    delete element.time;
                });

                res.json({data: result.data.auditDetLst, status: 200});
            }).catch( (err) => {
                res.json({error:err.toString(), status: 500});  })
        }
        catch(err){
            console.log(err)
            res.json({error:err.toString(), status: 500});   
        }

    },

    writeAudit: async (param) => {
        try{
            
            console.log('Saving now!');
            console.log(param);
            axios.post(audUrl + 'audit/save', null, { params: param}).then((result) => {
                // res.status(200);
                // res.json({data: result.data, status: 200});
                return {data: result.data, status: 200}
            }).catch((err) => { //res.json({error:err.toString(), status: 500})
                return {error:err.toString(), status: 500}
            } )
        }
        catch(err){
            return {error:err.toString(), status: 500} ;   
        }

    },

}
