# scapsulators
Spring 2022 Project

# Authentication Microservice
# Functionality/Motivation :
* The main purpose of this microservice is to perform all user login actions.
* The motivation to make a seperate microservice for uuthentication purpose is that we consider this as a different unit of function from other microservices which will only deal with the login functionality of the user. 

# Working :
* This microservice is written in java and uses spring boot.
* It has three main functions : 1) to authenticate the user when he/she is logging in, 2) tosave data of the user when registering, 3) Allowing the user to change his/her password by checking the security answer question.
* Other microservices can access these two functionalities of this microsevice by using REST API and the response is returned in a JSON format.
* We chose REST because it is stateless and the data is not tied to resources or methods, so REST can handle multiple types of calls, return different data formats and even change structurally with the correct implementation of hypermedia.

# Installation :
* Software Required : Docker - 20.10.12 (You can get docker from https://docs.docker.com/get-docker/)
* To start the microservice : 
* Step 1 - Built the services : audit/build_auditService.sh, authentication/build-authenticationService.sh, dbconnection/build-dbService.sh
* Step 2 - Start all java based microservices - start-allServices.sh
* The audit microservice runs on port - 8081

* To run the test cases - 
* Software Required - JDK-15 (You can get JDK-15 from https://www.oracle.com/java/technologies/javase/jdk15-archive-downloads.html)
* Command - mvnw test

# Implmentation Status : 
* This microservice uses REST to communicate with other microservices(written in a programming language other than Java) and uses Spring's web client to communicate with other spring based microservices.
* We will be implementing Open ID COnnect for authentication in the future.

# Team : 
<img src="Documentation/Team-members/Rutuja.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>
- **Rutuja Jadhav**: Rutuja is a final year Master's student studying at Indiana University Bloomington, majoring in Computer Science. She has full time experience as an Full stack software engineer for around 4 years. With this course, she intends to gain a deeper understanding of concepts in Distributed Systems and understand how to develop end to end applications on distributed systems.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/rutuja-jadhav-89284a126/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/RutujaJadhav19/)