import json
import random
import time
from kafka import KafkaProducer
from datetime import datetime, timedelta
from Data_Generator.data_generator import generate_user_behavior_data, generate_content_metadata, generate_platform_usage_data, generate_derived_metrics

# Kafka Producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Change to your Kafka broker's address if not running locally
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize the data into JSON
)

# data generation functions timestamps
def generate_timestamp():
    return (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()

# Function to send generated synthetic data to Kafka topic 'generate-synthetic-data'
def send_data_to_kafka():
    while True:
        # Generate data using your existing methods
        user_behavior = generate_user_behavior_data()  
        content_metadata = generate_content_metadata()  
        platform_usage = generate_platform_usage_data()  
        derived_metrics = generate_derived_metrics(user_behavior)  

        # Consolidating all the generated data into a single dictionary
        synthetic_data = {
            "User Behavior Data": user_behavior,
            "Content Metadata": content_metadata,
            "Platform Usage Data": platform_usage,
            "Derived Metrics": derived_metrics,
        }

        # Send the generated data to the Kafka topic 'generate-synthetic-data'
        producer.send('generate-synthetic-data', value=synthetic_data)
        producer.flush()  # Ensure the data is sent to Kafka immediately

        # Log the generated data to console for monitoring
        print(synthetic_data)

        # Pause for 10 seconds before sending the next data
        time.sleep(10)

# Start sending synthetic data continuously to Kafka
send_data_to_kafka()
