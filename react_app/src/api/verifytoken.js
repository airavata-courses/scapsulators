import axios from 'axios';
import { url } from '../config';


async function verifyToken(token) {



var data = JSON.stringify({"token":token});

var config = {
  method: 'get',
  url: `http://${url}/api/verifySession`,
  headers: { 
    'Content-Type': 'application/json'
  },
  data: data
};

console.log('hello', token);
var res = await axios(config).then(function (response) {
    console.log(response);
    return response;
});

console.log(res);
return res;
    
}

export { verifyToken}