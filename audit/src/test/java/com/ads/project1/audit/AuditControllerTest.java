package com.ads.project1.audit;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;

import com.ads.project1.audit.models.OutputBody;
import com.ads.project1.audit.models.OutputBodyAuditFetch;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
public class AuditControllerTest {
	
	@LocalServerPort
	private int port;

	@Autowired
	private TestRestTemplate restTemplate;

	@Test
	public void auditSave() throws Exception {
		assertThat(this.restTemplate.postForObject("http://localhost:" + port + "/audit/save", String.class,
				OutputBody.class));
	}
	
	@Test
	public void auditFetch() throws Exception {
		assertThat(this.restTemplate.getForObject("http://localhost:" + port + "/audit/fetch",
				OutputBodyAuditFetch.class));
	}

}
