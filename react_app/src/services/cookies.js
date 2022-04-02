import Cookies from 'universal-cookie';



function setCookie(token, profile){
    const cookies = new Cookies();
    cookies.set('accessToken', token, { path: '/' });
    cookies.set('email', profile['email'], { path: '/' });
    cookies.set('name', profile['name'], { path: '/' });
    cookies.set('givenName', profile['givenName'], { path: '/' });
    cookies.set('familyName', profile['familyName'], { path: '/' });
}


function getCookie(){

    const cookies = new Cookies();

    const email = cookies.get('email');
    const name = cookies.get('name');
    const givenName = cookies.get('givenName');
    const familyName = cookies.get('familyName');
    const accessToken = cookies.get('accessToken');
    
    return {email: email, name: name, givenName: givenName,  familyName: familyName, accessToken: accessToken };

}

function deleteCookie(){
    const cookies = new Cookies();
    cookies.set('accessToken', null, { path: '/' });
}




export {setCookie, getCookie, deleteCookie}