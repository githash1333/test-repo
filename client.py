from kafka import KafkaAdminClient
from kafka.admin import NewTopic

# Define the Kafka server
bootstrap_servers = '192.168.56.1:9092'

# Create an AdminClient instance
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Define the topic name and configuration
topic_name = 'test_topic'
num_partitions = 1
replication_factor = 1

# Create a new topic
new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)

# Create the topic
try:
    admin_client.create_topics(new_topics=[new_topic], validate_only=False)
    print(f'Topic "{topic_name}" created successfully.')
except Exception as e:
    print(f'Failed to create topic "{topic_name}": {e}')
finally:
    # Close the AdminClient
    admin_client.close()