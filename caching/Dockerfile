FROM openjdk:latest
ADD target/caching-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8086
ENTRYPOINT ["java","-jar","/app.jar"]