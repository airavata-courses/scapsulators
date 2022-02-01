package com.ads.project1.databaseconnect.controller;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.logging.Logger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.ads.project1.databaseconnect.model.Audit;
import com.ads.project1.databaseconnect.model.AuditFetch;
import com.ads.project1.databaseconnect.model.OutputBody;
import com.ads.project1.databaseconnect.model.OutputBodyAuditFetch;
import com.ads.project1.databaseconnect.model.User;
import com.ads.project1.databaseconnect.service.DatabaseService;

@RestController
@RequestMapping("/database")
public class DatabaseController {
	
	private static final Logger logger = Logger.getLogger(DatabaseController.class.getName());		
	@Autowired
	DatabaseService dbService;
	
	@RequestMapping("/authenticate/{username}/{password}")
	public OutputBody autheticateUser(@PathVariable("username") String username, @PathVariable("password") String password) {
		
		OutputBody status = dbService.authenticateUser(username, password);
		return status ;
	}
	
	
	@RequestMapping("/signup/{username}/{password}/{firstName}/{lastName}/{city}/{state}/{secQtAns}/{emailAdd}")
	public OutputBody signup(@PathVariable("username") String username, @PathVariable("password") String password,@PathVariable("firstName") String firstName, @PathVariable("lastName") String lastName,  @PathVariable("city") String city, @PathVariable("state") String state, @PathVariable("secQtAns") String secQtAns, @PathVariable("emailAdd") String emailAdd) {
		User user = new User(username, password, firstName, lastName, city, state, secQtAns, emailAdd);
		OutputBody status = dbService.signUp(user);
		return status ;
	}
	
	
	@RequestMapping("/forgotpassword/{username}/{secQtAns}")
	public OutputBody forgotpassword(@PathVariable("username") String username, @PathVariable("secQtAns") String secQtAns) {
		OutputBody status = dbService.forgotPassword(username, secQtAns);
		return status ;
	}
	
	@RequestMapping("/updatepassword/{username}/{password}")
	public OutputBody updatepassword(@PathVariable("username") String username, @PathVariable("password") String password) {
		OutputBody status = dbService.updatepassword(username, password);
		return status ;
	}
	
	@RequestMapping(value = "/auditsave", method = RequestMethod.POST)
	public OutputBody auditsave(@RequestParam("username") String username, @RequestParam("date") String date, @RequestParam("time") String time, @RequestParam("nexradstation") String nexradstation ) {
		Audit audit = new Audit(username, date, time, nexradstation, getCurrentDate());
		logger.info("DATA RECEIVED = "+ audit.getUsername()+ " "+ audit.getDate()+ " "+ audit.getTime()+ " "+ audit.getNexradStation()+  "  "+ audit.getNexradStation());
		OutputBody status = dbService.auditsave(audit);
		return status ;
	}
	
	@RequestMapping("/auditfetch/{username}")
	public OutputBodyAuditFetch auditfetch(@PathVariable("username") String username) {
		OutputBodyAuditFetch auditDetails = dbService.auditfetch(username);
		return auditDetails ;
	}
	
	public String getCurrentDate() {
		Date date = new Date();  
	    SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");  
	    String currentDate = formatter.format(date);  
	    return currentDate;
	}
	
	
}
