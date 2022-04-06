package com.ads.caching;

import java.util.logging.Logger;

import org.json.JSONObject;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import com.ads.caching.entity.NASAData;

@Service
public class KafkaConsumer {
	private static final Logger logger = Logger.getLogger(KafkaConsumer.class.getName());	
	
	   public static NASAData consumerData = new NASAData("-1","","");
	   public static String consumerDataString;
	   public static JSONObject consumerDataJSON;
	
	   @KafkaListener(topics = "WEATHER_REPORT",  groupId = "caching_NASA", containerFactory = "studentListner")
	   public void publish(byte[] data)
	   {
		   try {
			   logger.info("CachingApplication ::  KafkaConsumer : Consuming the butes");
			   logger.info("CachingApplication ::  KafkaConsumer : Data consumed : "+new String(data));
		   
		   
			   JSONObject dataInJSON=new JSONObject(new String(data));
			   consumerDataString = new String(data);
			   consumerDataJSON = dataInJSON;		  
		   
			   KafkaConsumer.consumerData.setId("1");
			   logger.info("CONSUMERDATA AFTER: " + consumerData.getId());
		   }
		   catch(Exception e) {
			   logger.info("CachingApplication :: KafkaConsumer : Error in consuming");
			   e.printStackTrace();
			   consumerDataString = "FAIL";
		   }
	   }

}
