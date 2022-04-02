const {
    register,
    login,
    forgot,
    updatepass
  } = require("../controllers/authenticate");

const {verify} = require('../controllers/sessions');

const verifyToken = require("../helpers/verifyToken");

  const {
    getImg
  } = require("../controllers/weather");

  const {
    getAudit,
    writeAudit
  } = require("../controllers/audit");

const express = require("express");
const router = express.Router();

//authentication api's
router.post("/login", login);
router.post("/register", register);
router.post("/forgot", forgot);
router.post("/updatepass", updatepass);

//session api's
router.post("/verifySession", verify);


//python nexrad api
router.post("/getimg", getImg);

//user audit api
router.post("/getaudit",verifyToken, getAudit);
router.post("/writeaudit", writeAudit);

module.exports = router;