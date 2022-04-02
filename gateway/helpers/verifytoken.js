const createErrror = require('http-errors');
const { OAuth2Client } = require('google-auth-library')


const client = new OAuth2Client(process.env.CLIENT_ID)

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

module.exports = verifyToken;