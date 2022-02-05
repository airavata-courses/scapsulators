package com.ads.project1.databaseconnect.repository;


import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import com.ads.project1.databaseconnect.model.User;

public interface UserRepository extends MongoRepository<User, String>{
	
	@Query("{username:'?0'}")
    User findItemByUsername(String username);
	
	
	
    

}
