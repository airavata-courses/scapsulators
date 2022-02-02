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

import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/login")
public class AuthenticationController {
	
	private static final Logger logger = Logger.getLogger(AuthenticationController.class.getName());
	
	@Autowired
	private WebClient.Builder webClientBuilder;
	
	@RequestMapping(value = "/authenticate", method = RequestMethod.POST,consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	public Mono<OutputBody> autheticateUser(@RequestBody MultiValueMap body) {
		
		String username = body.get("username").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String password = body.get("password").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		Mono<OutputBody> status = webClientBuilder.build().get().uri("http://database-connect:8082/database/authenticate/" + username + "/"+ password).retrieve().bodyToMono(OutputBody.class);
		//Mono<String> status = webClientBuilder.build().get().uri("http://localhost:8082/database/authenticate/" + username + "/"+ password).retrieve().bodyToMono(String.class);
			
		return status;
	}
	
	
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
		
		
		Mono<OutputBody> status = webClientBuilder.build().get().uri("http://database-connect:8082/database/signup/" + username + "/"+ password + "/" + firstName + "/" + lastName + "/" + city + "/" + state + "/" + secQtAns + "/" + emailAdd).retrieve().bodyToMono(OutputBody.class);
			
		return status;
	}
	
	
	@RequestMapping(value = "/forgotpassword", method = RequestMethod.POST,consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	public Mono<OutputBody> forgotpassword(@RequestBody MultiValueMap body) {
		String username = body.get("username").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String secQtAns = body.get("secQtAns").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		
		Mono<OutputBody> status = webClientBuilder.build().get().uri("http://database-connect:8082/database/forgotpassword/" + username + "/"+ secQtAns).retrieve().bodyToMono(OutputBody.class);
		return status ;
	}
	
	
	@RequestMapping(value = "/updatepassword", method = RequestMethod.POST,consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	public Mono<OutputBody> updatepassword(@RequestBody MultiValueMap body) {
		String username = body.get("username").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		String password = body.get("password").toString().replaceAll("\\[", "").replaceAll("\\]", "");
		
		
		Mono<OutputBody> status = webClientBuilder.build().get().uri("http://database-connect:8082/database/updatepassword/" + username + "/"+ password).retrieve().bodyToMono(OutputBody.class);
		return status ;
	}
	
	
	
		
}
