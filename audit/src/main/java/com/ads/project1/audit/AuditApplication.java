package com.ads.project1.audit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.reactive.function.client.WebClient;

@SpringBootApplication
public class AuditApplication {
	
	@Bean
	public WebClient.Builder getWebClientBuilder(){
		return WebClient.builder();
	}
	

	public static void main(String[] args) {
		SpringApplication.run(AuditApplication.class, args);
	}

}
