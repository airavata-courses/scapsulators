# Connecting Flask Producer with Flask Consumer

## Pre-requisites:

### Firing up Kafka Server using Docker:
```
> Docker-kafka-startup\start-kafka.bat

> Docker-kafka-startup\create-topics.bat
```


## Running the Flask applications
```
> pip install -r requirements.txt

> cd Flask-producer/ 

> startup.bat

In new terminal run:

> cd Flask-consumer/ 

> startup.bat


Open the consumer endpoint in browser (http://localhost:5001/consumeTopicFromProducer); it'll wait for a message from Kafka-topic to show up from Producer application.

Open the producer endpoint in browser (http://localhost:5000/pushTopicToConsumer); it'll generate a GIF image -> send it to the consumer -> consumer will read these bytes of data and regenerate the GIF.

The message has been delivered over an asynchronous message queue system via Kafka.
```