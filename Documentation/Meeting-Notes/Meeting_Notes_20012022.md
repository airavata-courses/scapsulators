# 20th Jan 2022:

## Use-case:

Implementing a distributed weather-tracking system of microservices. AWS NEXRAD use level-2 data for ease of access.


## Updates:

	Chose Kafka for inter-microservice communication over gRPC/REST: Kafka is Asynchronous and great for real-life publish/subscribe applications without distributed clocking.
	Setup project structure on GitHub - DONE
	Raise initial issues for build ideas - IN PROGRESS
	All 3 folks research on use case, datasets available - DONE
	All 3 folks conduct a POC: Send message from client-to-server and vice versa via Kafka as a streaming service- DONE
	Shubham- identified Dockerfile of template image for starting NodeJS builds. Interservice communication POC still pending.
	Potential add-ons to final Project-1:
		Add User's locality weather details on Homepage.
		Popular/most frequently searched locations on Homepage audit table of searches.
		Add hyperlink to audit table to retrieve previously visualized requests.
	Rutuja- Drew up initial-plans for microservices architecture, system design and task-list.


### Sprint plan (14 days) - Next regroup on 21st Jan:

	Raise initial issues for build ideas.
	All 3 folks conduct a POC: Send image message from server-to-client via Kafka as a streaming service. Backend framework candidates-
		Shubham: Nodejs/Flask
		Rutuja: Spring/Java
		Vikrant: Flask/SpringBoot
	Read about buildfiles: Makefile for Python Flask, Gradle vs Maven for Java Spring/SpringBoot.
	Sit together and draw up wireframes for UI registration, login, homepage, Search, and Visualization.
	Draw up User-centric napkin diagrams for easy understanding: What does it do? If it does X, who will use it?
	Vikrant- POC for Python quick S3 data access, parsing and image generation based on requested parameters. Needs to upload code for Flask + Kafka application.
	Shubham- POC for Flask to React communication. Needs to upload Dockerfile for Nodejs + Kafka application.
	Rutuja- POC for Java authentication and user creation- create MongoDB connection as well.