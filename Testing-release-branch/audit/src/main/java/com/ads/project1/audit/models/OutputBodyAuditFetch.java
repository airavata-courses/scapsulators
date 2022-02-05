package com.ads.project1.audit.models;

import java.util.List;

public class OutputBodyAuditFetch {
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

	public List<AuditFetch> getAuditDetLst() {
		return auditDetLst;
	}

	public void setAuditDetLst(List<AuditFetch> auditDetLst) {
		this.auditDetLst = auditDetLst;
	}

	private String message;
	
	private String status;
	
	List<AuditFetch> auditDetLst;

	public OutputBodyAuditFetch(String message, String status, List<AuditFetch> auditDetLst) {
		super();
		this.message = message;
		this.status = status;
		this.auditDetLst = auditDetLst;
	}
	
	public OutputBodyAuditFetch() {}
	
	

}
