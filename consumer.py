from kafka import KafkaConsumer
import json

# Define the Kafka server and topic
bootstrap_servers = '192.168.56.1:9092'
topic_name = 'test_topic'

# Create a Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',  # Start reading at the earliest message
    enable_auto_commit=True,
    group_id='notification-group',  # Consumer group ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON
)

# Read messages
try:
    print(f"Listening for messages on topic '{topic_name}'...")
    for message in consumer:
        notification_payload = message.value  # Get the deserialized message
        print(f'Received notification: {notification_payload}')
except Exception as e:
    print(f'Error consuming messages: {e}')
finally:
    # Close the consumer
    consumer.close()