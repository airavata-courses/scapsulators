package com.ads.project1.audit.controller;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.logging.Logger;
import java.util.stream.Stream;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.MediaType;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;

import com.ads.project1.audit.models.Audit;
import com.ads.project1.audit.models.AuditFetch;
import com.ads.project1.audit.models.OutputBody;
import com.ads.project1.audit.models.OutputBodyAuditFetch;

import reactor.core.publisher.Mono;


@RestController
@RequestMapping("/audit")
@Service
public class AuditController {
	private static final Logger logger = Logger.getLogger(AuditController.class.getName());	

	private static final String TOPIC = "test";

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;
    
	@Autowired
	private WebClient.Builder webClientBuilder;
	
	public void sendMessage(String message) {
        logger.info(String.format("#### -> Producing message -> %s", message));
        this.kafkaTemplate.send(TOPIC, message);
    }
	
	
	@RequestMapping(value = "/save", method = RequestMethod.POST)
	public OutputBody saveAudit (@RequestParam("username") String username, @RequestParam("date") String date, @RequestParam("time") String time, @RequestParam("nexradstation") String nexradstation) {
		//logger.info("DATA RECEIVED IN AUDIT = "+ username+ " "+ date+ " "+ time+  "  "+ nexradstation);
		//Mono<OutputBody> status = webClientBuilder.build().post().uri("http://database-connect:8082/database/auditsave?username="+username+"&date="+date+"&time="+time+"&nexradstation="+nexradstation).retrieve().bodyToMono(OutputBody.class);
		//Mono<String> status = webClientBuilder.build().post().uri("http://database-connect/database/auditsave?username="+username+"&date="+date+"&time="+time+"&nexradstation="+nexradstation).retrieve().bodyToMono(String.class);
		Date currdate = Calendar.getInstance().getTime();  
		DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd hh:mm:ss");  
		String strDate = dateFormat.format(currdate);  

		String sendMessage = username+"#"+date+"#"+time+"#"+nexradstation;
		sendMessage(sendMessage);
		//return status;
		OutputBody status = new OutputBody("SUCCESS","200");
		return status;
	}
	
	@RequestMapping(value = "/fetch", method = RequestMethod.GET)
	public Mono<OutputBodyAuditFetch> signup (@RequestParam("username") String username) {
		
		Mono<OutputBodyAuditFetch> auditDetails = webClientBuilder.build().get().uri("http://database-connect:8082/database/auditfetch/" + username).retrieve().bodyToMono(OutputBodyAuditFetch.class);
		return auditDetails; 
		
		
	}
	


    
	

  

}
