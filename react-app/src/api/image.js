import axios from 'axios';

async function getData(body) {

      delete body['state'];
      console.log('sending', body);
      
      var config = {
        method: 'post',
        url: 'http://localhost:5000/api/getimg',
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