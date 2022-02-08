package com.ads.project1.databaseconnect.database;

import java.util.List;
import java.util.logging.Logger;

import org.springframework.beans.factory.annotation.Autowired;

import com.ads.project1.databaseconnect.contants.Constants;
import com.ads.project1.databaseconnect.model.Audit;
import com.ads.project1.databaseconnect.model.AuditFetch;
import com.ads.project1.databaseconnect.model.OutputBody;
import com.ads.project1.databaseconnect.model.OutputBodyAuditFetch;
import com.ads.project1.databaseconnect.model.User;
import com.ads.project1.databaseconnect.repository.AuditRepository;
import com.ads.project1.databaseconnect.repository.UserRepository;

public class DatabaseConnectionImpl implements DatabaseConnection{
	
	private static final Logger logger = Logger.getLogger(DatabaseConnectionImpl.class.getName());
	
	@Autowired
	UserRepository userDetailsRepo;
	
	@Autowired
	AuditRepository auditDetailsRepo;
	
	
	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To save the user details when he/she is signing up for our application.
	 * Author            - Rutuja Jadhav  
	 */

	@Override
	public OutputBody signUp(User user) {
		try {
			logger.info("User creation started for "+user.getUsername()+" ...");
						
			if(checkUserExists(user.getUsername())) {
				return new OutputBody(Constants.EXISTS, Constants.status_201);				
			}			
			
			userDetailsRepo.save(new User(user.getUsername(), user.getPassword(), user.getFirstName(), user.getLastName(), user.getCity(), user.getState(), user.getSecurtyQtAnswer(), user.getEmailAdd()));
			logger.info("User creation completed for "+user.getUsername()+" ...");
			
			
			return new OutputBody(Constants.SUCCESS, Constants.status_200);
		
		} catch(Exception e) {
			logger.info("Error while creating username "+user.getUsername());
			e.printStackTrace();
			return new OutputBody(Constants.FAIL, Constants.status_404);
		}
	}
	
       
       public boolean checkUserExists(String username) {
    	   try {
    		   logger.info("Checking if the user exists for username : " + username);
    		   User user = new User();
    		   user = userDetailsRepo.findItemByUsername(username);
          
    		   if (user != null) {
    			   return true;
    		   }
    	   	}catch(Exception e) {
    		   logger.info("ERROR while checking if the user exists for username : " + username);
    		   e.printStackTrace();
    	   }
           
           return false;
       }
     

       

    /*
   	 * Input Parameters  - MultiValueMap
   	 * Output Parameters - OutputBody : message, status 
   	 * Purpose           - To authenticate the user details when he/she is logging into our application
   	 * Author            - Rutuja Jadhav  
   	 */

   	@Override
   	public OutputBody authenticateUser(String username, String password) {
   		try {
   			logger.info("Authenticating user : " + username);
   			if(!checkUserExists(username)) {
   				return new OutputBody(Constants.NOTEXISTS, Constants.status_202);			
			}	
   			User user = new User();
            user = userDetailsRepo.findItemByUsername(username);

            logger.info("Authenticating user Complete : " + username);
            return new OutputBody(user.getPassword(), Constants.status_200);

   		}catch(Exception e) {
   			logger.info("ERROR while authenticating the user : " + username);
   			e.printStackTrace();
   			return new OutputBody(Constants.FAIL, Constants.status_404);
   		}

   		
   	}
   	
   	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To check the security question answer to allow the user to change his/her password.
	 * Author            - Rutuja Jadhav  
	 */
  
	@Override
	public OutputBody forgotPassword(String username, String secQtAns) {
		try {
			if(!checkUserExists(username)){
				return new OutputBody(Constants.NOTEXISTS, Constants.status_202);
			}
			logger.info("Checking Security Answers for username : " + username);
			User user = new User();
			user = userDetailsRepo.findItemByUsername(username);
			if(user.getSecurtyQtAnswer().equals(secQtAns))
				return new OutputBody(Constants.SUCCESS, Constants.status_200);
		}catch(Exception e) {
			logger.info("ERROR while retriving forgotpassword for userName : " + username);
   			e.printStackTrace();
   			return new OutputBody(Constants.FAIL, Constants.status_404);
		}
		
		return new OutputBody(Constants.FAILFORGOTPASSWORD, Constants.status_405);
	}


	
	

	/*
	 * Input Parameters  - MultiValueMap
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To update the password.
	 * Author            - Rutuja Jadhav  
	 */

	@Override
	public OutputBody updatepassword(String username, String password) {		
        
        try {
        	logger.info("Updating password for username : " + username);
        	User user = userDetailsRepo.findItemByUsername(username);
        	user.setPassword(password);        
        
        	User userStatus = new User();
        	userStatus = userDetailsRepo.save(new User(user.getUsername(), user.getPassword(), user.getFirstName(), user.getLastName(), user.getCity(), user.getState(), user.getSecurtyQtAnswer(), user.getEmailAdd()));
		   
        	if (userStatus != null) {
        		return new OutputBody(Constants.SUCCESS, Constants.status_200);
        	}
        	}catch(Exception e) {
        		logger.info("ERROR while updating password for userName : " + username);
        		e.printStackTrace();
        		return new OutputBody(Constants.FAIL, Constants.status_404);
        	
        	}
		return new OutputBody(Constants.FAIL, Constants.status_404);
		
		   
	}


	
	
	/*
	 * Input Parameters  - username, date, time, nexradstation
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To save user data for auditory purpose
	 * Author            - Rutuja Jadhav  
	 */

	@Override
	public OutputBody auditsave(Audit audit) {
		try {
			logger.info("Audit creation started for "+audit.getUsername()+" ...");
			
			auditDetailsRepo.save(new Audit(audit.getUsername(), audit.getDate(), audit.getTime(), audit.getNexradStation(), audit.getCurrentDate()));
			logger.info("Audit creation completed for "+audit.getUsername()+" ...");			
			
			return new OutputBody(Constants.SUCCESS, Constants.status_200);
		
		} catch(Exception e) {
			logger.info("Error while saving audit details for username :  "+audit.getUsername());
			e.printStackTrace();
			return new OutputBody(Constants.FAIL, Constants.status_404);
		}		
		
	}


	
	/*
	 * Input Parameters  - username, date, time, nexradstation
	 * Output Parameters - OutputBody : message, status 
	 * Purpose           - To save user data for auditory purpose
	 * Author            - Rutuja Jadhav  
	 */

	@Override
	public OutputBodyAuditFetch auditfetch(String username) {
		try {
			logger.info("Audit fetch started for "+username+" ...");
			
			List<AuditFetch> auditDetails = auditDetailsRepo.findItemByUsername(username);
			
			logger.info("Audit creation completed for "+username+" ...");			
			
			return new OutputBodyAuditFetch(Constants.SUCCESS, Constants.status_200, auditDetails);
		
		} catch(Exception e) {
			logger.info("Error while saving audit details for username :  "+username);
			e.printStackTrace();
			return new OutputBodyAuditFetch(Constants.FAIL, Constants.status_404, null );
		}		
		
		
		   
	}


}
