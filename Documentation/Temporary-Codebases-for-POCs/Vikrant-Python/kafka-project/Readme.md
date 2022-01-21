# Connecting Flask application (Producer) with Kafka Consumer

## Pre-requisites:
```
Navigate to the folder where *kafka* was extracted on your local machine.

Run the zookeeper-service in one terminal:
> bin\windows\zookeeper-server-start.bat config\zookeeper.properties

In new terminal run the kafka-service:
> bin\windows\kafka-server-start.bat config\server.properties
```


## Running the Flask application (Producer) and Consumer
```
> pip install -r requirements.txt

> python app.py

In new terminal run:
> python kafka-consumer.py

From postman invoke the endpoint with appropriate message json-body: localhost:9092/kafka/pushToConsumers
If error, check the *app.py* code.

Your terminal that's running kafka-consumer.py should show the exact same message as json-body.
```