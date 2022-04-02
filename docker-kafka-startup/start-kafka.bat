docker-compose rm -svf
docker-compose up

# docker exec -it kafka kafka-console-producer --broker-list localhost:9092 --topic WEATHER_REPORT
# docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic WEATHER_REPORT