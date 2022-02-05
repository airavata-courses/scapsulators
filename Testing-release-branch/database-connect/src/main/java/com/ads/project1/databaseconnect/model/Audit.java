package com.ads.project1.databaseconnect.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document("audit")
public class Audit {
	

	public Audit(String username, String date, String time, String nexradStation, String currentDate) {
		super();
		this.username = username;
		this.date = date;
		this.time = time;
		this.nexradStation = nexradStation;
		this.currentDate = currentDate;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getDate() {
		return date;
	}

	public void setDate(String date) {
		this.date = date;
	}

	public String getTime() {
		return time;
	}

	public void setTime(String time) {
		this.time = time;
	}

	public String getNexradStation() {
		return nexradStation;
	}

	public void setNexradStation(String nexradStation) {
		this.nexradStation = nexradStation;
	}

	private String username;
	
	private String date;
	
	private String time;
	
	private String nexradStation;
	
	private String currentDate;

	public String getCurrentDate() {
		return currentDate;
	}

	public void setCurrentDate(String currentDate) {
		this.currentDate = currentDate;
	}

}
