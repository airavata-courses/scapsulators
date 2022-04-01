package com.ads.project1.databaseconnect.repository;

import java.util.List;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import com.ads.project1.databaseconnect.model.GroceryItem;


public interface ItemRepository extends MongoRepository<GroceryItem, String>{
	@Query("{name:'?0'}")
    GroceryItem findItemByName(String name);
    
    @Query(value="{category:'?0'}", fields="{'name' : 1, 'quantity' : 1}")
    List<GroceryItem> findAll(String category);
    
    public long count();
	

}
