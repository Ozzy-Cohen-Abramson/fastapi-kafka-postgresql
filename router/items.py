from typing import List
from fastapi import HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from starlette import status
from models.Item import ItemSchema
from utils import schemas
from fastapi import APIRouter
from utils.database import get_db
from utils.kafka_producer import produce_kafka_message

router = APIRouter(
    prefix='/items',
    tags=['Items']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.ItemResponse])
def produce_item(item_item: schemas.CreateItem, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):

    new_item = ItemSchema(**item_item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    background_tasks.add_task(produce_kafka_message, new_item, 'item_created')
    return [new_item]

@router.get('/', response_model=List[schemas.ItemResponse])  # Use ItemResponse schema
def get_items(db: Session = Depends(get_db)):
    items = db.query(ItemSchema).all()
    
    return items  # FastAPI will convert SQLAlchemy objects to Pydantic response

@router.get('/{id}', response_model=schemas.ItemResponse, status_code=status.HTTP_200_OK)
def get_item_by_id(id:int ,db:Session = Depends(get_db)):

    idv_item = db.query(ItemSchema).filter(ItemSchema.id == id).first()

    if idv_item is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idv_item

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_item_by_id(id:int, db:Session = Depends(get_db)):

    deleted_item = db.query(ItemSchema).filter(ItemSchema.id == id)


    if deleted_item.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    deleted_item.delete(synchronize_session=False)
    db.commit()


@router.put('/{id}', response_model=schemas.ItemResponse, status_code=status.HTTP_200_OK)
def update_item_by_id(update_item:schemas.ItemBase, id:int, background_tasks: BackgroundTasks, db:Session = Depends(get_db)):

    updated_item =  db.query(ItemSchema).filter(ItemSchema.id == id)

    if updated_item.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    
    updated_item.update(update_item.dict(), synchronize_session=False)
    db.commit()
    
    background_tasks.add_task(produce_kafka_message, updated_item, 'item_updated')

    return  updated_item.first()
