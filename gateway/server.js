require('dotenv').config()
const express = require('express');
const morgan = require('morgan');
const httpError = require('http-errors');
const cors = require('cors');
const bodyParser = require('body-parser');
const allRoute = require("./routes/allRoute");
const app = express();

const PORT = process.env.PORT || 5000;

app.use(morgan('dev'));
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.use("/api", allRoute);


// middleware to catch uncaught errors
app.use((error, req, res, next) => {
    res.status(500);
    res.json({'error': error.toString()});
});

//middleware to catch undefined api routes
app.get('*',async function(req,res,next) {
    res.status(404);
    res.json({'status': 400, 'error': 'API not found'});
});

app.listen(5000, ()=> {
    console.log(`Process running in ${process.env.NODE_ENV} port ${process.env.PORT}`);
});

module.exports = app;




