const {
    register,
    login,
    forgot,
    updatepass
  } = require("../controllers/authenticate");

  const {
    getImg
  } = require("../controllers/weather");

  const {
    getAudit,
    writeAudit
  } = require("../controllers/audit");

const express = require("express");
const router = express.Router();


router.post("/login", login);
router.post("/register", register);
router.post("/forgot", forgot);
router.post("/updatepass", updatepass);

router.post("/getimg", getImg);

router.post("/getaudit", getAudit);
router.post("/writeaudit", writeAudit);

module.exports = router;