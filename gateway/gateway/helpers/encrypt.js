const bcrypt = require("bcryptjs");

module.exports = {
generateHash: function(password){
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);},

compareHash: function(p1,p2){
    return bcrypt.compareSync(p1, p2); }

}
