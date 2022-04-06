const {
    register,
    login,
    forgot,
    updatepass
  } = require("../controllers/authenticate");

const {verify} = require('../controllers/sessions');

//const verifyToken = require("../helpers/verifyToken");

  const {
    getImg
  } = require("../controllers/weather");

  const {getnasaData} = require("../controllers/nasadata");

  const {
    getAudit,
    writeAudit
  } = require("../controllers/audit");

const express = require("express");
const router = express.Router();

const verifyToken = async (req,res,next) =>{
  try {

const token = req.headers.authorization;
if(!token) {res.json({error:"Unauthorized!", status: 500});
  return
};
const ticket = await client.verifyIdToken({ 
      idToken: token,
      audience: process.env.CLIENT_ID
  }); 
  console.log(ticket['payload']['email']);
}

  catch(err){
      res.json({error:err.toString(), status: 500});
      return
  }
next()
}


//authentication api's
router.post("/login", login);
router.post("/register", register);
router.post("/forgot", forgot);
router.post("/updatepass", updatepass);

//session api's
router.post("/verifySession", verify);


//python nexrad api
router.post("/getimg", getImg);

//nasa data
router.post("/getnasa", getnasaData);

//user audit api
router.post("/getaudit",verifyToken, getAudit);
router.post("/writeaudit", writeAudit);

module.exports = router;