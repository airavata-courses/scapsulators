package com.ads.caching;

import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;

import com.ads.caching.entity.NASAData;
import com.ads.caching.repository.NASADao;

@SpringBootApplication
@RestController
@RequestMapping("/caching")
public class CachingApplication {
	
	private static final Logger logger = Logger.getLogger(CachingApplication.class.getName());	
	
	private static final String TOPIC = "REQUEST_REPORT";
	
	@Autowired
    private KafkaTemplate<String, NASAData> kafkaTemplate;
	
	@Autowired
	private WebClient.Builder webClientBuilder;

	public static void main(String[] args) {
		SpringApplication.run(CachingApplication.class, args);
	}
	
	@Autowired
    private NASADao dao;

    @PostMapping("/save")
    public String save(@RequestBody NASAData product) {
    	try {
    		logger.info("CachingApplication :: CachingApplication : Looking in cache");
    		String response = findProduct(product.getTimestamp()+"@"+product.getVisualize());
    		logger.info("RESPONSE = "+response);   	
    		logger.info("Sending = PRODUCING################"+product.getTimestamp());
    		logger.info("Sending = PRODUCING################"+product.getVisualize());
    		if(response == null || response.equals("")) {
    			logger.info("CachingApplication :: CachingApplication : Cache Miss");
    			sendMessage(product);
    		
    		
    			logger.info("CachingApplication :: CachingApplication : Waiting for Kafka Consumer");
			logger.info("CachingApplication :: CachingApplication : Waiting for Consumer to consume data : "+KafkaConsumer.consumerData.getId());
    			while(KafkaConsumer.consumerData.getId().equals("-1")) {
    				
    			}
    			logger.info("CachingApplication :: CachingApplication : Saving to Redis");
    			logger.info("CachingApplication :: CachingApplication : Consumed in string in controller = "+KafkaConsumer.consumerDataString);

    			if(!(KafkaConsumer.consumerDataString.equals("FAIL") || KafkaConsumer.consumerDataString.contains("Sorry"))) {
    				dao.saveRedisObject(product.getTimestamp()+"@"+product.getVisualize(), KafkaConsumer.consumerDataString);
    			}
    		
        		
    			logger.info("CachingApplication :: CachingApplication : Saved in Cache");
    			return KafkaConsumer.consumerDataString;
    		}
    		else {
    			logger.info("CachingApplication :: CachingApplication : Cache Hit");
    			logger.info("CachingApplication :: CachingApplication : Response = "+response);
    	
    			JSONObject dataInJSON=new JSONObject(response);    	
    			return response;
    		}    	
    	}catch(Exception e) {
    		logger.info("CachingApplication :: CachingApplication : Error in Caching Application");
    		e.printStackTrace() ;
    		return "FAIL";
    	}
    	
    }
    
   
    
    public void sendMessage(NASAData product) {     
    	try {
    		logger.info("PRODUCING = in send message "+product.getVisualize());
    		logger.info("PRODUCING = in send message "+product.getTimestamp());
    		this.kafkaTemplate.send(TOPIC, product);
    	}catch(Exception e) {
    		logger.info("CachingApplication :: CachingApplication : Error in Caching Application in sendMessage");
    		e.printStackTrace() ;
    	}
    }

    

    
    public String findProduct(String key) {
    	try {    
    		logger.info("CachingApplication :: CachingApplication : Retrieving the object for key = "+key);
    		return dao.findCacheableObjectByKey(key);
    	}catch(Exception e) {
    		logger.info("CachingApplication :: CachingApplication : Error in Caching Application in findProduct");
    		e.printStackTrace() ;
    		return "FAIL";
    	}
    
    }
  

}
