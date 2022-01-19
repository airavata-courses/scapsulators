# 18th Jan 2022:

AWS NEXRAD use level-2 data for ease of access.

Use-case:
Need to finalize based on https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00345


### Sprint plan (16 days) - End date 20th Jan:
	Setup project structure on GitHub and raise initial issues for build ideas.
	All 3 folks research on use case, datasets available.
	All 3 folks conduct a POC Send message from client-to-server and vice versa via Kafka as a streaming service. Backend framework candidates-
		Shubham: Nodejs/Flask
		Rutuja: Spring/Java
		Vikrant: Flask/SpringBoot
	Shubham will researches on data and visualizing in React, sending messages via Kafka to microservice.
	Vikrant/Rutuja will research about number of microservices for authentication, data retrieval, communicating with API gateway, API gateway to UI, etc.
	Read about buildfiles: Makefile for Python Flask, Gradle vs Maven for Java Spring/SpringBoot.
	Sit together and draw up wireframes/napkin diagrams for UI registration, login, homepage, Search, and Visualization.
	Sit together and decide between gRPC vs Kafka vs REST (HTTP) for inter-microservice communication.
	