from kafka import KafkaProducer
from dotenv import main
import os
import json
from models.Item import ItemSchema


main.load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
KAFKA_TOPIC_ITEM_CREATED = os.getenv("KAFKA_TOPIC_ITEM_CREATED", "item_created")
KAFKA_TOPIC_ITEM_UPDATED = os.getenv("KAFKA_TOPIC_ITEM_UPDATED", "item_updated")

PRODUCER_CLIENT_ID = 'fastapi_producer'

def serializer(message):
    return json.dumps(message).encode()  # utf-8

producer = KafkaProducer(
    api_version=(0, 8, 0),
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=serializer,
    client_id=PRODUCER_CLIENT_ID
)

def produce_kafka_message(message_request: ItemSchema, topic: str):
    try:
        if topic == 'item_created':
            producer.send(KAFKA_TOPIC_ITEM_CREATED, json.dumps({
                'description': message_request.description,
                'name': message_request.name,
                'id': message_request.id
            }))
        elif topic == 'item_updated':
            producer.send(KAFKA_TOPIC_ITEM_UPDATED, json.dumps({
                'description': message_request.description,
                'name': message_request.name,
                'id': message_request.id
            }))
        else:
            raise ValueError("Invalid topic")

        producer.flush()  # make sure all of our messages are sent
    except Exception as error:
        # TODO: use better log system
        print(f"Error occurred: {error}")
