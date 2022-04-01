FROM openjdk:latest
ADD target/database-connect-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 30004
ENTRYPOINT ["java","-jar","/app.jar"]
