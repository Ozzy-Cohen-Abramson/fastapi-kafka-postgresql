from fastapi import FastAPI
from models.Item import ItemSchema 
import json
from utils.database import Base, engine
from router import items
from dotenv import main
import uvicorn
import os

main.load_dotenv()
port = int(os.getenv("PORT", 8000))  # Default port is 8000

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/health_check')
def check_health():
    return "API is running"

app.include_router(items.router)

if __name__ == "__main__":
    print(f"Starting FastAPI on http://127.0.0.1:{port}")
    uvicorn.run(app, host="localhost", port=port)