docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --config max.message.bytes=900000000 \
    --config replica.fetch.max.bytes=900000000 \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic test
