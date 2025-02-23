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

3. Build and start the services using Docker Compose:
   docker-compose up --build

4. The FastAPI application will be available at `http://localhost:8000`.

## Testing the Application

1. Access the Swagger UI at `http://localhost:8000/docs` to interact with the API endpoints.

2. Use the following endpoints:

- GET /items: Fetch all items
- POST /items: Create a new item
- GET /items/{id}: Fetch an item by ID
- PUT /items/{id}: Update an item
- DELETE /items/{id}: Delete an item

3. When you create or update an item, you should see the corresponding Kafka messages logged in the `kafka-consumer` service logs.

## Stopping the Application

To stop the application and remove the containers, run:
docker-compose down

To stop the application and remove the containers, volumes, and images, run:
docker-compose down -v --rmi all
