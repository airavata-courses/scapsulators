package com.ads.project1.databaseconnect;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

import com.ads.project1.databaseconnect.database.DatabaseConnection;
import com.ads.project1.databaseconnect.database.DatabaseConnectionImpl;
import com.ads.project1.databaseconnect.repository.UserRepository;
import com.ads.project1.databaseconnect.service.DatabaseService;
import com.ads.project1.databaseconnect.service.DatabaseServiceImpl;


@SpringBootApplication
@EnableMongoRepositories
public class DatabaseConnectApplication implements CommandLineRunner{
	
	@Bean
	public DatabaseService getDatabaseSeviceBuilder(){
		return new DatabaseServiceImpl();
	}
	
	@Bean
	public DatabaseConnection getDatabaseConnectionBuilder(){
		return new DatabaseConnectionImpl();
	}
	
	
	
	
	@Autowired
	UserRepository userDetailsRepo;
	
	public static void main(String[] args) {
		SpringApplication.run(DatabaseConnectApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		// TODO Auto-generated method stub
		//System.out.println("-------------CREATE GROCERY ITEMS-------------------------------\n");
        
		//createUser();
        
        //System.out.println("\n----------------SHOW ALL GROCERY ITEMS---------------------------\n");
        
        //showAllUserDet();
        
        /*System.out.println("\n--------------GET ITEM BY NAME-----------------------------------\n");
        
        getGroceryItemByName("Whole Wheat Biscuit");
        
        System.out.println("\n-----------GET ITEMS BY CATEGORY---------------------------------\n");
        
        getItemsByCategory("millets");
    
          System.out.println("\n-----------UPDATE CATEGORY NAME OF SNACKS CATEGORY----------------\n");
        
        updateCategoryName("snacks");    
                
        System.out.println("\n----------DELETE A GROCERY ITEM----------------------------------\n");
        
        deleteGroceryItem("Kodo Millet");
        
        System.out.println("\n------------FINAL COUNT OF GROCERY ITEMS-------------------------\n");
        
        findCountOfGroceryItems();
        
        System.out.println("\n-------------------THANK YOU---------------------------");*/
		
	}
	
	//CREATE
    /*void createUser() {
        System.out.println("Data creation started...");
        userDetailsRepo.save(new User("test1", "test1","Bloomington", "Indiana", "Dog", "rutjadhav1993@gmail.com"));
        userDetailsRepo.save(new User("test2", "test2","Bloomington", "Indiana", "Dog", "rutjadhav1993@gmail.com"));
        userDetailsRepo.save(new User("test3", "test3","Bloomington", "Indiana", "Dog", "rutjadhav1993@gmail.com"));
        
        
        /*groceryItemRepo.save(new GroceryItem("Whole Wheat Biscuit", "Whole Wheat Biscuit", 5, "snacks"));
        groceryItemRepo.save(new GroceryItem("Kodo Millet", "XYZ Kodo Millet healthy", 2, "millets"));
        groceryItemRepo.save(new GroceryItem("Dried Red Chilli", "Dried Whole Red Chilli", 2, "spices"));
        groceryItemRepo.save(new GroceryItem("Pearl Millet", "Healthy Pearl Millet", 1, "millets"));
        groceryItemRepo.save(new GroceryItem("Cheese Crackers", "Bonny Cheese Crackers Plain", 6, "snacks"));
        System.out.println("Data creation complete...");
    }
    
    public void showAllUserDet() {
        
   	 userDetailsRepo.findAll().forEach(item -> System.out.println(getItemDetails(item)));
    }
    
 // Print details in readable form
    
    public String getItemDetails(User item) {

        System.out.println(
        "User Name: " + item.getUsername() + 
        ", \nCity: " + item.getCity() +
        ", \nState: " + item.getState()
        );
        
        return "";
    }*/
    
    
    // READ
    // 1. Show all the data
    /* public void showAllUserDet() {
         
    	 userDetailsRepo.findAll().forEach(item -> System.out.println(getItemDetails(item)));
     }
     
     // 2. Get item by name
     public void getGroceryItemByName(String name) {
         System.out.println("Getting item by name: " + name);
         GroceryItem item = groceryItemRepo.findItemByName(name);
         System.out.println(getItemDetails(item));
     }
     
     // 3. Get name and quantity of a all items of a particular category
     public void getItemsByCategory(String category) {
         System.out.println("Getting items for the category " + category);
         List<GroceryItem> list = groceryItemRepo.findAll(category);
         
         list.forEach(item -> System.out.println("Name: " + item.getName() + ", Quantity: " + item.getQuantity()));
     }
     
     // 4. Get count of documents in the collection
     public void findCountOfGroceryItems() {
         long count = groceryItemRepo.count();
         System.out.println("Number of documents in the collection: " + count);
     }
     
 
     public void updateCategoryName(String category) {
         
         // Change to this new value
         String newCategory = "munchies";
         
         // Find all the items with the category snacks
         List<GroceryItem> list = groceryItemRepo.findAll(category);
         
         list.forEach(item -> {
             // Update the category in each document
             item.setCategory(newCategory);
         });
         
         // Save all the items in database
         List<GroceryItem> itemsUpdated = groceryItemRepo.saveAll(list);
         
         if(itemsUpdated != null)
             System.out.println("Successfully updated " + itemsUpdated.size() + " items.");         
     }
     
  // DELETE
     public void deleteGroceryItem(String id) {
         groceryItemRepo.deleteById(id);
         System.out.println("Item with id " + id + " deleted...");
     }*/

}
