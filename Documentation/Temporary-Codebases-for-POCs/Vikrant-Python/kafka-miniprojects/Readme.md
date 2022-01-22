# Connecting Flask Producer with Flask Consumer

## Pre-requisites:
```
Navigate to the folder where *kafka* was extracted on your local machine.

Run the zookeeper-service in one terminal:
> bin\windows\zookeeper-server-start.bat config\zookeeper.properties

In new terminal run the kafka-service:
> bin\windows\kafka-server-start.bat config\server.properties
```


## Running the Flask applications
```
> pip install -r requirements.txt

> cd flask-producer-app/ 

> set FLASK_APP=flask-producer-app

> set FLASK_ENV=development

> flask run --host=localhost --port=5000

In new terminal run:

> cd flask-consumer-app/ 

> set FLASK_APP=flask-consumer-app

> set FLASK_ENV=development

> flask run --host=localhost --port=5001


Open the consumer endpoint in browser (localhost:5001); it'll wait for a message from Kafka-topic to show up from Producer application.

From postman invoke the endpoint with appropriate message json-body: http://localhost:5000/pushTopicToConsumer

Your terminal that's running kafka-consumer should show the exact same message as json-body. The message has been delivered over an asynchronous message queue system via Kafka.
```