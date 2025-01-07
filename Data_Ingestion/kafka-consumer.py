from kafka import KafkaConsumer
import json

# Kafka Consumer configuration
consumer = KafkaConsumer(
    'generate-synthetic-data',
    bootstrap_servers='localhost:9092',
    group_id='synthetic-data-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
)

# print("Listening to 'generate-synthetic-data' topic...")

# Process incoming Kafka messages
for message in consumer:
    synthetic_data = message.value
    print("Consumed data from Kafka:", synthetic_data)
