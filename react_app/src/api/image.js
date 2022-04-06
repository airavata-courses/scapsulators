import axios from 'axios';
import { url } from '../config';
import { getCookie } from '../services/cookies';

async function getData(body, user) {
      delete body['state'];
      const userDetails = getCookie();
      console.log('sending', body);
      body['username'] = userDetails['email'];

      console.log(body);
      var config = {
        method: 'post',
        url: `http://${url}/api/getimg`,
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': userDetails.accessToken
        },
        data : body
      };
      
      return  axios(config)
      .then(function (response) {
        
        if(response.status === 200) {
        return {success: true, data: response.data } }
        else {
            return {success: false}
        }
      })
      .catch(function (error) {

        return {success: false}
      });

      
  }

export {getData}