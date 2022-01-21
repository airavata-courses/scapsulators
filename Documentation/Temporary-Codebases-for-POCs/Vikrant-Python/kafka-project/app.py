from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from kafka import KafkaProducer, KafkaConsumer
app = Flask(__name__)
TOPIC_NAME = 'INFERENCE'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER, 
    api_version = (0, 11, 15)
)


@app.route('/kafka/pushToConsumers', methods=['GET','POST'])
def kafka_producer():
    req_body = request.get_data()
    print(req_body, type(req_body), str(req_body))
    #json_payload = json.dumps(req_body)
    #json_payload_bytes = str.encode(json_payload)
    #print(json_payload_bytes)
    producer.send(TOPIC_NAME, req_body)
    producer.flush()
    print(f'Sent to consumer topic:{TOPIC_NAME} , message:{req_body}')
    return jsonify({ 'message':'Sent to consumer..' , 'status':'Pass' })


if __name__=='__main__':
    app.run(debug=True, port=5000)