# scapsulators
Spring 2022 Project

# Audit Microservice
# Functionality/Motivation :
* The main purpose of this microservice is to connect to the database and perform all transactions.
* The motivation to make a seperate microservice for database connection purpose is that we consider this as a different unit of function from other microservices which will only deal with the audit data of the user. 

# Working :
* This microservice is written in java and uses spring boot.
* It has four main functions : 1) to save the audit data in the database for a user and 2) to fetch the audit data from the database for a user. 3) to retrieve the user details for logging and audit purposes. 4) To save audit and sign up data in the database.
* Other microservices can access these two functionalities of this microsevice by using REST API and the response is returned in a JSON format.
* We chose REST because it is stateless and the data is not tied to resources or methods, so REST can handle multiple types of calls, return different data formats and even change structurally with the correct implementation of hypermedia.

# Installation :
* Software Required : 
* 1) Docker - 20.10.12 (You can get docker from https://docs.docker.com/get-docker/)
* 2) JDK 15 (You can get JDK-15 from https://www.oracle.com/java/technologies/javase/jdk15-archive-downloads.html)
* To start the microservice : 
* Step 1 - Go to the folder that contains the pom.xml file and open command prompt.
* Step 2 - Set JAVA_HOME = <Path to JDK folder>
*        - Set PATH = <JAVA_HOME/bin>
* Step 3 - Type Command - mvnw clean package
* Step 4 - Build the services : audit/build_auditService.sh, autehntication/build-authenticationService.sh, dbconnection/build-dbService.sh - (This will vreate a docker image).
* Step 5 - Start all java based microservices - start-allServices.sh
* The database microservice runs on port - 8082


# Implmentation Status : 
* This microservice uses REST to communicate with other microservices(written in a programming language other than Java) and uses Spring's web client to communicate with other spring based microservices.
* This microservice connects to Mongo DB to store and retrieve the details. We chose Mongo DB because it has high performance, MongoDB is designed from the ground up for ease of horizontal scale-out and is a NoSQL database which is a are non-tabular database and can store data differently than relational tables.

# Team : 
<img src="Documentation/Team-members/Rutuja.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>
- **Rutuja Jadhav**: Rutuja is a final year Master's student studying at Indiana University Bloomington, majoring in Computer Science. She has full time experience as an Full stack software engineer for around 4 years. With this course, she intends to gain a deeper understanding of concepts in Distributed Systems and understand how to develop end to end applications on distributed systems.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/rutuja-jadhav-89284a126/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/RutujaJadhav19/)