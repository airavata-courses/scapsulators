package com.ads.project1.authentication.controller;

import java.util.Map;
import java.util.logging.Logger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;

import com.ads.project1.authentication.models.OutputBody;
import com.ads.project1.authentication.models.User;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/login")
public class AuthenticationController {
	
	private static final Logger logger = Logger.getLogger(AuthenticationController.class.getName());
	
	@Autowired
	private WebClient.Builder webClientBuilder;
	

	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To authenticate the user details when he/she is logging into our application
	 * Author            - Rutuja Jadhav  
	 */
	@RequestMapping(value = "/authenticate", method = RequestMethod.POST,consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	public Mono<OutputBody> autheticateUser(@RequestBody MultiValueMap body) {
		String username = body.get("username").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String password = body.get("password").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		User user = new User(username, password, null, null, null, null, null, null);
		try {
			logger.info("AuthenticationController : Authenticating username = "+username);		
		Mono<OutputBody> status = webClientBuilder.build().post().uri("http://localhost:30004/database/authenticate").body(Mono.just(user), User.class).retrieve().bodyToMono(OutputBody.class);
		logger.info("AuthenticationController : Authenticatiopn complete for username = "+username);
		return status;
		} catch(Exception e) {
			logger.info("AuthenticationController : Error while authenticating username = "+username);
			e.printStackTrace();
			OutputBody error = new OutputBody("Internal Service Error", "404");
			return Mono.just(error);			
		}
	}
	
	
	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To save the user details when he/she is signing up for our application.
	 * Author            - Rutuja Jadhav  
	 */

	@RequestMapping(value = "/signup", method = RequestMethod.POST,consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)	
	public Mono<OutputBody> signup (@RequestBody MultiValueMap body) {
		String username = body.get("username").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String password = body.get("password").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String secQtAns = body.get("secQtAns").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String firstName = body.get("firstName").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String lastName = body.get("lastName").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String city = body.get("city").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String state = body.get("state").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		
		String emailAdd = body.get("emailAdd").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		
		User user = new User(username, password, firstName, lastName, city, state, secQtAns, emailAdd);
		
		try {
			logger.info("AuthenticationController : Signing Up username = "+username);		
		
			Mono<OutputBody> status = webClientBuilder.build().post().uri("http://localhost:30004/database/signup").body(Mono.just(user), User.class).retrieve().bodyToMono(OutputBody.class);
			logger.info("AuthenticationController : Signing Up Complete for username = "+username);		
			return status;
		}catch(Exception e) {
			logger.info("AuthenticationController : Error while signing up username = "+username);
			e.printStackTrace();
			OutputBody error = new OutputBody("Internal Service Error", "404");
			return Mono.just(error);			
		}
	}
	
	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To check the security question answer to allow the user to change his/her password.
	 * Author            - Rutuja Jadhav  
	 */

	@RequestMapping(value = "/forgotpassword", method = RequestMethod.POST,consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	public Mono<OutputBody> forgotpassword(@RequestBody MultiValueMap body) {
		String username = body.get("username").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String secQtAns = body.get("secQtAns").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		User user = new User(username, null, null, null, null, null, secQtAns, null);
		try {
			logger.info("AuthenticationController : In forgot password for username = "+username);		
		
			Mono<OutputBody> status = webClientBuilder.build().post().uri("http://localhost:30004/database/forgotpassword").body(Mono.just(user), User.class).retrieve().bodyToMono(OutputBody.class);
			logger.info("AuthenticationController : Forgot Password Complete for username = "+username);	
			return status ;
		}catch(Exception e) {
			logger.info("AuthenticationController : Error in forgot password for username = "+username);
			e.printStackTrace();
			OutputBody error = new OutputBody("Internal Service Error", "404");
			return Mono.just(error);			
		}
	}
	
	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To update the password.
	 * Author            - Rutuja Jadhav  
	 */

	@RequestMapping(value = "/updatepassword", method = RequestMethod.POST,consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	public Mono<OutputBody> updatepassword(@RequestBody MultiValueMap body) {
		
		String username = body.get("username").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String password = body.get("password").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		User user = new User(username, password, null, null, null, null, null, null);
		
		try {
			logger.info("AuthenticationController : Updating password for username = "+username);		
	
			Mono<OutputBody> status = webClientBuilder.build().post().uri("http://localhost:30004/database/updatepassword").body(Mono.just(user), User.class).retrieve().bodyToMono(OutputBody.class);
			logger.info("AuthenticationController : Update Password Complete for username = "+username);	
			return status ;
		}catch(Exception e){
			logger.info("AuthenticationController : Error while updating the password for username = "+username);
			e.printStackTrace();
			OutputBody error = new OutputBody("Internal Service Error", "404");
			return Mono.just(error);			
		}
	}
	
	
	
		
}
