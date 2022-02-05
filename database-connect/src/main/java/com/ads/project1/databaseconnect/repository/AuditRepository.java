package com.ads.project1.databaseconnect.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import com.ads.project1.databaseconnect.model.Audit;
import com.ads.project1.databaseconnect.model.AuditFetch;

public interface AuditRepository extends MongoRepository<Audit, String>{
	
	@Query(value = "{username:'?0'}", fields="{'date' : 1, 'time' : 1, 'nexradStation' : 1, 'currentDate' : 1}")
    List<AuditFetch> findItemByUsername(String username);
	

}
