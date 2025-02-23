<!-- # fastapi-kafka-postgresql

This is a simple FastAPI handling messages with6 routes.

To run locally:

1. python -m venv venv
2. source venv/Scripts/active
3. run: pip install -r ./requirements.txt
4. to run the server: fastapi dev main.py -->

# Inventory Management Service

This project implements a simple inventory management service using FastAPI, PostgreSQL, and Kafka. It provides a REST API for managing inventory items and uses Kafka for event-driven messaging.

## Architecture Overview

The application consists of the following components:

1. FastAPI application: Provides REST API endpoints for managing inventory items.
2. PostgreSQL database: Stores inventory item data.
3. Kafka: Handles event streaming for item creation and updates.
4. Kafka Consumer: Consumes messages from Kafka topics and logs events.

## Setup Instructions

1. Ensure you have Docker and Docker Compose installed on your system.

2. Clone this repository:
   https://github.com/Ozzy-Cohen-Abramson/fastapi-kafka-postgresql.git

3. Create a `.env` file in the root directory with the following content:

   PORT={8000}
   KAFKA_BOOTSTRAP_SERVERS={kafka:9092}
   KAFKA_TOPIC_ITEM_CREATED=item_created
   KAFKA_TOPIC_ITEM_UPDATED=item_updated

   POSTGRES_USER={suer}
   POSTGRES_PASSWORD={password}
   POSTGRES_DB={dbname}

4. Build and start the services using Docker Compose:
   docker-compose up --build

5. The FastAPI application will be available at `http://localhost:8000`.

## Project Structure

inventory_management_service/
├── models/
│ ├── item.py
├── router/
│ ├── items.py
├── utils/
│ ├── kafka_consumer.py
│ └── kafka_producer.py
│ └── database.py
│ └── schemas.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── init.sql
├── requirements.txt
└── README.md
└── .env
└── .gitignore

## Testing the Application

1. Access the Swagger UI at `http://localhost:8000/docs` to interact with the API endpoints.

2. Use the following endpoints:

   - GET /items: Fetch all items
   - POST /items: Create a new item
   - GET /items/{id}: Fetch an item by ID
   - PUT /items/{id}: Update an item
   - DELETE /items/{id}: Delete an item

3. When you create or update an item, you should see the corresponding Kafka messages logged in the `kafka-consumer` service logs.

4. The database is pre-populated with 10 dummy items representing characters from Star Wars and Lord of the Rings.

## Stopping the Application

To stop the application and remove the containers, run:
docker-compose down

To stop the application and remove the containers, volumes, and images, run:
docker-compose down -v --rmi all

## Troubleshooting

If you encounter any issues with Kafka connectivity, try the following:

1. Ensure all services are up and running:
   docker-compose ps

2. Check the logs of the Kafka and Zookeeper services:
   docker-compose logs kafka zookeeper

3. If needed, you can restart the Kafka consumer service:
   docker-compose restart kafka-consumer

## Contributing

Please feel free to submit issues, fork the repository and send pull requests!
