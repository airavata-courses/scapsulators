from kafka import KafkaConsumer
import json
from concurrent.futures import ThreadPoolExecutor

TOPIC_NAME = 'inference'
KAFKA_SERVER = 'localhost:9092'

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_SERVER,
    api_version=(0,11,15),
    value_deserializer=lambda msg: json.loads(msg.decode('utf-8'))
)

producer = KafkaConsumer(
    bootstrap_servers=KAFKA_SERVER,
    api_version=(0,11,15)
)


def process_inference(data):
    print(f'Received {data}...')


for inference in consumer:
    process_inference(inference)
