package com.ads.project1.databaseconnect.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document("user")
public class User {
	
	@Id
	private String username;
	
	private String password;
	
	private String firstName;
	
	private String lastName;
	
	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	private String city;
	
	private String state;
	
	private String securtyQtAnswer;
	
	private String emailAdd;

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	

	public String getSecurtyQtAnswer() {
		return securtyQtAnswer;
	}

	public void setSecurtyQtAnswer(String securtyQtAnswer) {
		this.securtyQtAnswer = securtyQtAnswer;
	}

	public String getEmailAdd() {
		return emailAdd;
	}

	public void setEmailAdd(String emailAdd) {
		this.emailAdd = emailAdd;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}



	public User(String username, String password, String firstName, String lastName, String city, String state,
			String securtyQtAnswer, String emailAdd) {
		super();
		this.username = username;
		this.password = password;
		this.firstName = firstName;
		this.lastName = lastName;
		this.city = city;
		this.state = state;
		this.securtyQtAnswer = securtyQtAnswer;
		this.emailAdd = emailAdd;
	}

	public User() {
	}

	
	
	
	

}
