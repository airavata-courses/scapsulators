import json
from kafka import KafkaConsumer

class Consumer:
    def __init__(self, topic_to_consume, kafka_server):
        self.consumer = KafkaConsumer(
            topic_to_consume,
            bootstrap_servers = kafka_server,
            api_version = (0, 11, 15),
            value_deserializer=lambda msg: json.loads(msg.decode('utf-8'))
        )

    def consume(self):
        for data in self.consumer:
            return data