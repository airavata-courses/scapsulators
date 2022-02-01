package com.ads.project1.audit.models;

public class OutputBody {

	
	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public OutputBody() {}

	public OutputBody(String message, String status) {
		super();
		this.message = message;
		this.status = status;
	}

	private String message;
	
	private String status;
	
	

}
