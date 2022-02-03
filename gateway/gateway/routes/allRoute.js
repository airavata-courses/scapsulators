const {
    register,
    login,
    forgot,
    updatepass
  } = require("../controllers/authenticate");

  const {
    getImg
  } = require("../controllers/weather");

const express = require("express");
const router = express.Router();


router.post("/login", login);
router.post("/register", register);
router.post("/forgot", forgot);
router.post("/updatepass", updatepass);

router.post("/getimg", getImg);

module.exports = router;