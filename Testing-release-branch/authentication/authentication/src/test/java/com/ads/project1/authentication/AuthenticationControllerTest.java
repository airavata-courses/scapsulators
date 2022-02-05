package com.ads.project1.authentication;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.util.MultiValueMap;

import com.ads.project1.authentication.models.OutputBody;


@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
public class AuthenticationControllerTest {

	@LocalServerPort
	private int port;

	@Autowired
	private TestRestTemplate restTemplate;

	@Test
	public void autheticateUser() throws Exception {
		assertThat(this.restTemplate.postForObject("http://localhost:" + port + "/login/authenticate", MultiValueMap.class,
				OutputBody.class));
	}
	
	@Test
	public void signup() throws Exception {
		assertThat(this.restTemplate.postForObject("http://localhost:" + port + "/audit/signup", MultiValueMap.class,
				OutputBody.class));
	}
	
	@Test
	public void forgotpassword() throws Exception {
		assertThat(this.restTemplate.postForObject("http://localhost:" + port + "/audit/forgotpassword", MultiValueMap.class,
				OutputBody.class));
	}
	
	@Test
	public void updatepassword() throws Exception {
		assertThat(this.restTemplate.postForObject("http://localhost:" + port + "/audit/updatepassword", MultiValueMap.class,
				OutputBody.class));
	}

}
