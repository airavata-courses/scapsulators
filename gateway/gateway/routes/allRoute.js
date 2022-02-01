const {
    register,
    login,
    forgot
  } = require("../controllers/authenticate");

  const {
    getImg
  } = require("../controllers/weather");

const express = require("express");
const router = express.Router();


router.post("/login", login);
router.post("/register", register);
router.post("/forgot", forgot);

router.get("/getimg", getImg);

module.exports = router;