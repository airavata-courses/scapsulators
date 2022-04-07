package com.ads.project1.databaseconnect.controller;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.logging.Logger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
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
@Service
public class DatabaseController {
	
	private static final Logger logger = Logger.getLogger(DatabaseController.class.getName());		
	@Autowired
	DatabaseService dbService;
	
	
	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To authenticate the user details when he/she is logging into our application
	 * Author            - Rutuja Jadhav  
	 */

	@RequestMapping(value = "/authenticate", method = RequestMethod.POST)
	public OutputBody autheticateUser(@RequestBody User body) {
		String username = body.getUsername();
		String password = body.getPassword();
	
		try {
				logger.info("DatabaseController Microservice : Authenticating user = "+ username);
			
		
		OutputBody status = dbService.authenticateUser(username, password);
		logger.info("DatabaseController Microservice : Successfully authenticated the user" );
		return status ;
		} catch(Exception e) {
			logger.info("DatabaseController : Error while authenticating username = "+username);
			e.printStackTrace();
			OutputBody error = new OutputBody("Internal Service Error", "404");
			return error;			
		}
	}
	

	@KafkaListener(topics = "test", groupId = "group_id")
    public void consume(String message) throws IOException {
		String parts[] = message.split("#");
		String username = parts[0];
		String date = parts[1];
		String time = parts[2];
		String  nexradstation = parts[3];
		Audit audit = new Audit(username, date, time, nexradstation, getCurrentDate());
		logger.info("DATA RECEIVED = "+ audit.getUsername()+ " "+ audit.getDate()+ " "+ audit.getTime()+ " "+ audit.getNexradStation()+  "  "+ getCurrentDate());
		OutputBody status = dbService.auditsave(audit);
        logger.info(String.format("#### -> Consumed message -> %s", message));
    }
	
	
	
	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To save the user details when he/she is signing up for our application.
	 * Author            - Rutuja Jadhav  
	 */

	@RequestMapping(value = "/signup", method = RequestMethod.POST)
	public OutputBody signup(@RequestBody User body) {
		String username = body.getUsername();
		String password = body.getPassword();
		String firstName = body.getFirstName();
		String lastName = body.getLastName();
		String city = body.getCity();
		String state = body.getState();
		String secQtAns = body.getSecurtyQtAnswer();
		String emailAdd = body.getEmailAdd();
		try {
			logger.info("DatabaseController Microservice : Signing up user = "+ username);
			User user = new User(username, password, firstName, lastName, city, state, secQtAns, emailAdd);
			OutputBody status = dbService.signUp(user);
			logger.info("DatabaseController Microservice : Successfully signing up user = "+ username);
			return status ;
		}catch(Exception e) {
				logger.info("DatabaseController : Error while signing up username = "+username);
				e.printStackTrace();
				OutputBody error = new OutputBody("Internal Service Error", "404");
				return error;			
			}
	}
	
	
	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To check the security question answer to allow the user to change his/her password.
	 * Author            - Rutuja Jadhav  
	 */

	@RequestMapping(value = "/forgotpassword", method = RequestMethod.POST)
	public OutputBody forgotpassword(@RequestBody User body) {
		String username = body.getUsername();
		String secQtAns = body.getSecurtyQtAnswer();
		try {
			logger.info("DatabaseController Microservice :In forgotpassword for user = "+ username);
		
		OutputBody status = dbService.forgotPassword(username, secQtAns);
		logger.info("DatabaseController Microservice : Completed forgotpassword for user = "+ username);
		
		return status ;
		}catch(Exception e) {
			logger.info("DatabaseController : Error in forgot password for username = "+username);
			e.printStackTrace();
			OutputBody error = new OutputBody("Internal Service Error", "404");
			return error;			
		}
	}
	
	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To update the password.
	 * Author            - Rutuja Jadhav  
	 */

	@RequestMapping(value = "/updatepassword", method = RequestMethod.POST)
	public OutputBody updatepassword(@RequestBody User body) {
		String username = body.getUsername();
		String password = body.getPassword();
		try {
			logger.info("DatabaseController Microservice : Updating the password for user = "+ username);
		
		OutputBody status = dbService.updatepassword(username, password);
		logger.info("DatabaseController Microservice : Completed Updating the password for user = "+ username);
		
		return status ;
		}catch(Exception e) {
			logger.info("DatabaseController : Error in Update password for username = "+username);
			e.printStackTrace();
			OutputBody error = new OutputBody("Internal Service Error", "404");
			return error;			
		}
	}
	
	/*
	 * Input Parameters  - username, date, time, nexradstation
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To save user data for auditory purpose
	 * Author            - Rutuja Jadhav  
	 */


	@RequestMapping(value = "/auditsave", method = RequestMethod.POST)
	public OutputBody auditsave(@RequestParam("username") String username, @RequestParam("date") String date, @RequestParam("time") String time, @RequestParam("nexradstation") String nexradstation ) {
		Audit audit = new Audit(username, date, time, nexradstation, getCurrentDate());
		logger.info("DATA RECEIVED = "+ audit.getUsername()+ " "+ audit.getDate()+ " "+ audit.getTime()+ " "+ audit.getNexradStation()+  "  "+ audit.getNexradStation());
		OutputBody status = dbService.auditsave(audit);
		return status ;
	}
	

  
  /*
	 * Input Parameters  - username
	 * Output Parameters - OutputBodyAuditFetch : message, status, auditDetails
	 * Purpose           - To fetch user's audit data
	 * Author            - Rutuja Jadhav  
	 */

	@RequestMapping("/auditfetch/{username}")
	public OutputBodyAuditFetch auditfetch(@PathVariable("username") String username) {
		OutputBodyAuditFetch auditDetails = dbService.auditfetch(username);
		return auditDetails ;
	}
	
	
	/*
	 * Input Parameters  - username
	 * Output Parameters - String
	 * Purpose           - To return the current date
	 * Author            - Rutuja Jadhav  
	 */

	public String getCurrentDate() {
		Date date = new Date();  
	    SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");  
	    String currentDate = formatter.format(date);  
	    return currentDate;
	}
	
	
}
