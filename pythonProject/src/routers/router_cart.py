from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text, update, delete, func
from src.database import get_session, Session

from src.schemas.schema_cart import CartCreate
from src.models import cart

router = APIRouter(
    prefix="/carts",
    tags=["cart"]
)


@router.get("/count")
def get_cart_count(db: Session = Depends(get_session)):
    stmt = db.query(cart).count()
    return {"result": stmt}


@router.get("/all")
def get_all_cart(db: Session = Depends(get_session)):
    stmt = select(cart)
    result = db.execute(stmt).all()
    result = [row._asdict() for row in result]
    return result


@router.post("/add")
def add_cart(new_cart: CartCreate, db: Session = Depends(get_session)):
    stmt = insert(cart).values(**new_cart.dict())
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}


@router.put("/update")
def update_cart(old_name: str, new_name: str, new_sum: int, new_product_component: CartCreate,
                db: Session = Depends(get_session)):
    stmt = update(cart).where(cart.c.name == old_name).values(name=new_name, sum=new_sum)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}


@router.delete("/delete")
def update_cart(old_name: str, db: Session = Depends(get_session)):
    stmt = delete(cart).where(cart.c.name == old_name)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}
# def get_specific_operations(session: get_session):
#     query = select(cart).where(cart.id == 1)
#     result = Session.execute(query)
#     return result.all()