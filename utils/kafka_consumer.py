from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import json
import os
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
KAFKA_TOPIC_ITEM_CREATED = os.getenv("KAFKA_TOPIC_ITEM_CREATED", "item_created")
KAFKA_TOPIC_ITEM_UPDATED = os.getenv("KAFKA_TOPIC_ITEM_UPDATED", "item_updated")

def create_consumer(max_retries=10, retry_delay=5):
    for i in range(max_retries):
        try:
            logger.info(f"Attempting to connect to Kafka (attempt {i+1}/{max_retries})...")
            consumer = KafkaConsumer(
                KAFKA_TOPIC_ITEM_CREATED,
                KAFKA_TOPIC_ITEM_UPDATED,
                bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
                auto_offset_reset="earliest",
                enable_auto_commit=True,
                group_id="inventory-group",
                value_deserializer=lambda x: json.loads(x.decode("utf-8")),
                api_version=(0, 10)
            )
            logger.info("Successfully connected to Kafka")
            return consumer
        except NoBrokersAvailable:
            logger.warning(f"No brokers available. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        except Exception as e:
            logger.error(f"Failed to connect to Kafka: {str(e)}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    raise Exception("Failed to connect to Kafka after multiple retries")

def run_consumer():
    logger.info("Kafka consumer started. Waiting for messages...")
    try:
        consumer = create_consumer()
        for message in consumer:
            logger.info(f"Received message: {message.topic}")
            logger.info(f"Message value: {message.value}")
    except Exception as e:
        logger.error(f"Error in Kafka consumer: {str(e)}")

if __name__ == "__main__":
    run_consumer()