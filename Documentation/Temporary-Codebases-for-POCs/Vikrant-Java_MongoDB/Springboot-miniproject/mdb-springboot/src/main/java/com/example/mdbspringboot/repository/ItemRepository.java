package com.example.mdbspringboot.repository;

import java.util.ArrayList;

import com.example.mdbspringboot.model.GroceryItem;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface ItemRepository extends MongoRepository<GroceryItem,String>{
    @Query(value="{name:'?0'}")
    GroceryItem findGroceryItemByName(String name);

    @Query(value="{category:'?0'}", fields="{'name':1, 'quantity':1}")
    ArrayList<GroceryItem> findAllGroceryItems(String category);

    public long count();

}
