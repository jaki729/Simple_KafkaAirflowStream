import json
import time
from kafka import KafkaConsumer
from datetime import datetime
from process_functions import process_user_behavior_data, store_in_mysql

# Kafka Consumer Configuration
consumer = KafkaConsumer(
    'generate-synthetic-data',           # Kafka topic
    bootstrap_servers='localhost:9092',  # Kafka broker address
    group_id='synthetic-data-consumer-group',  # Consumer group ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON messages
)

def flink_streaming_pipeline():
    """
    Processes incoming Kafka messages, processes the data, and stores it in MySQL.
    """
    print("Kafka consumer initialized. Listening for messages...")

    for message in consumer:
        try:
            # Extract data from the message
            user_behavior = message.value.get('User Behavior Data', {})
            content_metadata = message.value.get('Content Metadata', {})
            platform_usage = message.value.get('Platform Usage Data', {})
            derived_metrics = message.value.get('Derived Metrics', {})

            # Validate if user behavior contains required data
            if not user_behavior:
                print(f"Missing User Behavior Data in message: {message.value}")
                continue

            # Process user behavior data
            processed_data = process_user_behavior_data(
                user_behavior, content_metadata, platform_usage, derived_metrics
            )

            # Store the processed data in MySQL
            store_in_mysql(processed_data)

            # Log successful storage
            print(f"Processed and stored data: {processed_data}")

            # Simulate delay for real-time processing
            time.sleep(10)  

        except json.JSONDecodeError as json_err:
            print(f"Error decoding JSON message: {json_err}")
        except KeyError as key_err:
            print(f"Missing key in message: {key_err}")
        except Exception as e:
            print(f"Unexpected error during message processing: {e}")

# Entry point to start the Kafka consumer pipeline
if __name__ == "__main__":
    try:
        flink_streaming_pipeline()
    except KeyboardInterrupt:
        print("Stream processing interrupted by user. Exiting...")
    except Exception as e:
        print(f"Error initializing the pipeline: {e}")