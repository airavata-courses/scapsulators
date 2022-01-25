package com.example.mdbspringboot;

import java.util.List;
import com.example.mdbspringboot.model.GroceryItem;
import com.example.mdbspringboot.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

@SpringBootApplication
@EnableMongoRepositories
public class MdbSpringbootApplication implements CommandLineRunner {

	@Autowired
	ItemRepository groceryItemRepository;

	public static void main(String[] args) {
		SpringApplication.run(MdbSpringbootApplication.class, args);
	}

	
	public String getItemDetails(GroceryItem item){
		return "Item Id: "+item.getId()+
		"\nItem name: "+item.getName()+
		"\nItem category: "+item.getCategory()+
		"\nItem quantity: "+item.getQuantity();
	}
	
    public void createGroceryItems(){
        System.out.println("Creation of 5 random grocery-items...");
		groceryItemRepository.save(new GroceryItem("Biscuits-1", "Parle-G Biscuits", "snacks", 5));
		groceryItemRepository.save(new GroceryItem("Chicken-2", "Kroger's chicken wings", "lunch", 1));
		groceryItemRepository.save(new GroceryItem("Beers-3", "Apple Orchard Strong Cider", "drinks", 30));
		groceryItemRepository.save(new GroceryItem("Beers-4", "Miller Strong", "drinks", 6));
		groceryItemRepository.save(new GroceryItem("Beers-5", "Moonshine Cider", "drinks", 6));
		groceryItemRepository.save(new GroceryItem("Wine-6", "Chateau de faguette", "drinks", 1));
        System.out.println("Added all 5 grocery-items!");
    }


	public void showAllGroceryItems(){
		groceryItemRepository.findAll().forEach(item -> System.out.println(getItemDetails(item)));
	}

	public void getGroceryItemByName(String name){
		System.out.println("Getting item details for name: "+name);
		GroceryItem item = groceryItemRepository.findGroceryItemByName(name);
		System.out.println(getItemDetails(item));
	}

	public void getGroceryItemsByCategory(String category){
		System.out.println("Getting item details for category: "+category);
		List<GroceryItem> items = groceryItemRepository.findAllGroceryItems(category);
		items.forEach(item -> System.out.println(getItemDetails(item)));
	}


	public void findCountGroceryItems(){
		long count = groceryItemRepository.count();
		System.out.println("There are "+count+"item details in your grocery-list...");
	}


	public void updateCategoryName(String category){
		System.out.println("Retrieving all documents from DB with category: "+category);
		String newCategory = "munchies";
		List<GroceryItem> items = groceryItemRepository.findAllGroceryItems(category);
		items.forEach(item -> {
			item.setCategory(newCategory);
		});

		List<GroceryItem> updatedItems = groceryItemRepository.saveAll(items);
		if (updatedItems!=null){
			System.out.println("Updated documents in DB with old-category: "+category+" , to new-category: "+newCategory);
		}
		else{
			System.out.println("Something went wrong while trying to update...");
		}
	}

	public void deleteGroceryItem(String id){
		groceryItemRepository.deleteById(id);
		System.out.println("Deleted the grocery-item with ID: "+id);
	}


	@Override
	public void run(String... args) throws Exception {
		System.out.println("x");
		
		System.out.println("\n--------------------1. CREATING NEW LIST OF GROCERY ITEMS--------------------");
		createGroceryItems();

		System.out.println("\n--------------------2. SHOW ALL GROCERY ITEMS--------------------");
		showAllGroceryItems();

		System.out.println("\n--------------------3. GET GROCERY ITEM BY NAME--------------------");
		getGroceryItemByName("Miller Strong");

		System.out.println("\n--------------------4. GET GROCERY ITEMS BY CATEGORY--------------------");
		getGroceryItemsByCategory("snacks");

		System.out.println("\n--------------------5. UPDATE CATEGORY OF GROCERY ITEMS--------------------");
		updateCategoryName("snacks");

		System.out.println("\n--------------------6. DELETE GROCERY ITEM BY ID--------------------");
		deleteGroceryItem("Beers-3");

		System.out.println("\n--------------------7. FINAL COUNT OF GROCERY ITEMS--------------------");
		findCountGroceryItems();

		System.out.println("\n--------------------8. FINAL LIST OF GROCERY ITEMS--------------------");
		showAllGroceryItems();
		
	}

}