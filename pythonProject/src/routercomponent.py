from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text, update, delete, func
from src.database import get_session, Session
from src.models import ProductComponentCreate, product_component,product_type

router = APIRouter(
    prefix="/productcomponent",
    tags=["productcomponent"]
)
# @router.get("/type")
# def get_productcomponent_type(db: Session = Depends(get_session)):
#     stmt = text("""
#                     select  product_component.name, product_type.name
#                     from product_component
#                     inner join product_type
#                     on product_type_id = product_type.id
#                 """)
#     result = db.execute(stmt).scalars().all()
#     return result

@router.get("/ram")
def get_ram_component(db: Session = Depends(get_session)):
    stmt = select(product_component.c.name).where(product_component.c.product_type_id ==3)
    result = db.execute(stmt).scalars().all()
    return result


@router.get("/video")
def get_video_component(db: Session = Depends(get_session)):
    stmt = select(product_component.c.name).where(product_component.c.product_type_id ==2)
    result = db.execute(stmt).scalars().all()
    return result

@router.get("/all")
def get_ordered_component(db: Session = Depends(get_session)):
    stmt = select(product_component).order_by(product_component.c.cost)
    result = db.execute(stmt).all()
    result = [row._asdict() for row in result]
    return result

@router.post("/add")
def add_product_component(new_product_component: ProductComponentCreate,db: Session = Depends(get_session)):
    stmt = insert(product_component).values(**new_product_component.dict())
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.put("/update")
def update_product_component(old_name:str,pti: int,new_name:str,new_cost: int,db: Session = Depends(get_session)):
    stmt = update(product_component).where(product_component.c.name == old_name).values(product_type_id = pti,name = new_name, cost = new_cost)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.delete("/delete")
def delete_product_component(old_name:str,db: Session = Depends(get_session)):
    stmt = delete(product_component).where(product_component.c.name == old_name)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}