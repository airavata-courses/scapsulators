package com.ads.project1.audit.models;

public class AuditFetch {
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

	

	public AuditFetch(String date, String time, String nexradStation, String currentDate) {
		super();
		this.date = date;
		this.time = time;
		this.nexradStation = nexradStation;
		this.currentDate = currentDate;
	}
	
	public AuditFetch(String date, String time, String nexradStation, String currentDate, String username) {
		super();
		this.date = date;
		this.time = time;
		this.nexradStation = nexradStation;
		this.currentDate = currentDate;
		this.username = username;
	}
	
	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public AuditFetch() {}

	public String getNexradStation() {
		return nexradStation;
	}

	public void setNexradStation(String nexradStation) {
		this.nexradStation = nexradStation;
	}
}
