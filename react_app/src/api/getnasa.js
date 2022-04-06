import axios from 'axios';
import { url } from '../config';
import { getCookie } from '../services/cookies';

async function getNasaData(params){
    const userDetails = getCookie();
    var config = {
        method: 'post',
        url: `http://${url}/api/getnasa`,
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': userDetails.accessToken
        },
        data : JSON.stringify(params)
      };

      return  axios(config)
      .then(function (response) {
        
        if(response.data.status === 200) {
        return {success: true, data: response.data.data } }
        else {
            return {success: false}
        }
      })
      .catch(function (error) {

        return {success: false}
      });
}

export {getNasaData}