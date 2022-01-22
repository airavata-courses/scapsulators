import Kafka from 'node-rdkafka';
import eventType from '../eventType.js';
import * as fs from 'fs';

function saveImage(filename, data){
  var myBuffer = new Buffer(data.length);
  for (var i = 0; i < data.length; i++) {
      myBuffer[i] = data[i];
  }
  fs.writeFile(filename, myBuffer, function(err) {
      if(err) {
          console.log(err);
      } else {
          console.log("The file was saved!");
      }
  });
}

var consumer = new Kafka.KafkaConsumer({
  'group.id': 'kafka',
  'metadata.broker.list': 'localhost:9092',
}, {});

consumer.connect();

consumer.on('ready', () => {
  console.log('consumer ready..')
  consumer.subscribe(['test']);
  consumer.consume();
}).on('data', function(data) {
  //var new_d = String.fromCharCode(...data.value);
  //console.log('received', new_d);
  saveImage('./myimg.png', data.value)
  //console.log(`received message: ${eventType.fromBuffer(data.value)}`);
});
