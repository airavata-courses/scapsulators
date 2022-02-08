package com.ads.project1.audit.controller;

import java.util.Arrays;
import java.util.List;
import java.util.logging.Logger;
import java.util.stream.Stream;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;

import com.ads.project1.audit.models.AuditFetch;
import com.ads.project1.audit.models.OutputBody;
import com.ads.project1.audit.models.OutputBodyAuditFetch;

import reactor.core.publisher.Mono;


@RestController
@RequestMapping("/audit")
public class AuditController {
	private static final Logger logger = Logger.getLogger(AuditController.class.getName());	

	@Autowired
	private WebClient.Builder webClientBuilder;
	
	@RequestMapping(value = "/save", method = RequestMethod.POST)
	public Mono<OutputBody> signup (@RequestParam("username") String username, @RequestParam("date") String date, @RequestParam("time") String time, @RequestParam("nexradstation") String nexradstation) {
		logger.info("DATA RECEIVED IN AUDIT = "+ username+ " "+ date+ " "+ time+  "  "+ nexradstation);
		Mono<OutputBody> status = webClientBuilder.build().post().uri("http://database-connect:8082/database/auditsave?username="+username+"&date="+date+"&time="+time+"&nexradstation="+nexradstation).retrieve().bodyToMono(OutputBody.class);
		//Mono<String> status = webClientBuilder.build().post().uri("http://database-connect/database/auditsave?username="+username+"&date="+date+"&time="+time+"&nexradstation="+nexradstation).retrieve().bodyToMono(String.class);
			
		return status;
	}
	
	@RequestMapping(value = "/fetch", method = RequestMethod.GET)
	public Mono<OutputBodyAuditFetch> signup (@RequestParam("username") String username) {
		
		Mono<OutputBodyAuditFetch> auditDetails = webClientBuilder.build().get().uri("http://database-connect:8082/database/auditfetch/" + username).retrieve().bodyToMono(OutputBodyAuditFetch.class);
		return auditDetails; 
		
		
	}


}
