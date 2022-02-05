package com.ads.project1.databaseconnect.service;

import java.util.List;
import java.util.logging.Logger;

import org.springframework.beans.factory.annotation.Autowired;

import com.ads.project1.databaseconnect.database.DatabaseConnection;
import com.ads.project1.databaseconnect.model.Audit;
import com.ads.project1.databaseconnect.model.AuditFetch;
import com.ads.project1.databaseconnect.model.OutputBody;
import com.ads.project1.databaseconnect.model.OutputBodyAuditFetch;
import com.ads.project1.databaseconnect.model.User;



public class DatabaseServiceImpl implements DatabaseService{
	
	private static final Logger logger = Logger.getLogger(DatabaseServiceImpl.class.getName());
	
	@Autowired
	DatabaseConnection dbConnection;

	@Override
	public OutputBody signUp(User user) {
		
		OutputBody status = dbConnection.signUp(user);
		return status;
	}

	@Override
	public OutputBody authenticateUser(String username, String password) {
		OutputBody status = dbConnection.authenticateUser(username, password);
		return status;
	}

	@Override
	public OutputBody forgotPassword(String username, String secQtAns) {
		OutputBody status = dbConnection.forgotPassword(username, secQtAns);
		return status;
	}

	@Override
	public OutputBody updatepassword(String username, String password) {
		OutputBody status = dbConnection.updatepassword(username, password);
		return status;
	}

	@Override
	public OutputBody auditsave(Audit audit) {
		OutputBody status = dbConnection.auditsave(audit);
		return status;
	}

	@Override
	public OutputBodyAuditFetch auditfetch(String username) {
		OutputBodyAuditFetch auditDetails = dbConnection.auditfetch(username);
		return auditDetails;
	}

}
