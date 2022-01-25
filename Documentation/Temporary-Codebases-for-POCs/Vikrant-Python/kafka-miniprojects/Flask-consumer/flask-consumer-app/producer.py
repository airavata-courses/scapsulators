from kafka import KafkaProducer

class Producer():
    
    def __init__(self, kafka_server='localhost:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers = kafka_server,
            api_version = (0, 11, 15),
            #value_serializer=lambda m: pickle.dumps(m).encode('ascii')
            )
    
    def publish(self, topic, message):
        self.producer.send(topic, message)
        self.producer.flush()
