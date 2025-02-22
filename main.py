from fastapi import FastAPI
from item_schema import ItemSchema
import json

#  constants
app = FastAPI()

@app.get('/items')
async def get_items():
    print('Going to get items from PostgreSQL')
    # some logic to get items
    return {'message': 'Here are your items'}

@app.get('/items/{item_id}')
async def get_item_by_id(item_id: str):
    print(f'Going to get item with id {item_id}')
    
    # some logic to get items
    return {"item_id": item_id}

@app.post('/items/')
async def produce_item(item: ItemSchema):
    print(item)
    return {'message': 'Item received!'}

@app.put('/items/{item_id}')
async def update_item_by_id(item_id: str, item: ItemSchema):
    print(f'Updating item with id {item_id}')
    print(item)
    return {'message': 'Item updated!'}
    
@app.delete('/items/{item_id}')
async def delete_item_by_id(item_id: str):
    print(f'Deleting item with id {item_id}')
    return {'message': 'Item deleted!'}
    