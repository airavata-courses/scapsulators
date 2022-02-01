package com.ads.project1.databaseconnect.service;

import java.util.List;

import com.ads.project1.databaseconnect.model.Audit;
import com.ads.project1.databaseconnect.model.AuditFetch;
import com.ads.project1.databaseconnect.model.OutputBody;
import com.ads.project1.databaseconnect.model.OutputBodyAuditFetch;
import com.ads.project1.databaseconnect.model.User;

public interface DatabaseService {
	
	public OutputBody signUp(User user);

	public OutputBody authenticateUser(String username, String password);

	public OutputBody forgotPassword(String username, String secQtAns);

	public OutputBody updatepassword(String username, String password);

	public OutputBody auditsave(Audit audit);

	public OutputBodyAuditFetch auditfetch(String username);


}
