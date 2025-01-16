from kafka import KafkaProducer
import json
import time
from datetime import datetime

# Define the Kafka server and topic
bootstrap_servers = '192.168.56.1:9092'
topic_name = 'test_topic'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))  # Serialize JSON

# Function to create a notification payload

def create_notification_payload(notification_id, user_id, message, notification_type, status):
    return {
        "notification_id": notification_id,
        "user_id": user_id,
        "message": message,
        "timestamp": datetime.utcnow().isoformat() + 'Z',  # UTC timestamp
        "type": notification_type,
        "status": status
    }



# Send notification messages
try:
    for i in range(10):
        notification_payload = create_notification_payload(
            notification_id=str(i),
            user_id="67890",
            message=f"Your order {i} has been shipped!",
            notification_type="order_update",
            status="sent"
        )
        
        producer.send(topic_name, value=notification_payload)  # Send the notification payload
        print(f'Sent: {notification_payload}')
        time.sleep(1)  # Sleep for a second between messages
except Exception as e:
    print(f'Error sending message: {e}')
finally:
    # Close the producer
    producer.close()