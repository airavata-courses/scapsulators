import axios from 'axios';

async function getData(body, user) {
      const url = process.env.React_App_gateway_url;
      delete body['state'];
      console.log('sending', body);
      body['username'] = user;
      var config = {
        method: 'post',
        url: `http://${url}/api/getimg`,
        headers: { 
          'Content-Type': 'application/json'
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