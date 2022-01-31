const {
    register,
    login,
    forgot
  } = require("../controllers/authenticate");

const express = require("express");
const router = express.Router();


router.post("/login", login);
router.post("/register", register);
router.post("/forgot", forgot);

module.exports = router;