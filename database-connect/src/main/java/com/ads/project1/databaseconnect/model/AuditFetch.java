package com.ads.project1.databaseconnect.model;

public class AuditFetch {
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

	public String getNexradStation() {
		return nexradStation;
	}

	public void setNexradStation(String nexradStation) {
		this.nexradStation = nexradStation;
	}
}
