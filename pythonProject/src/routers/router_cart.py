from fastapi import APIRouter, Depends
from sqlalchemy import insert

from src.database import get_session, Session
from src.services.cart_service import CartService
from src.models import Product,Service
from src.schemas.schema_cart import CartCreate,CartUpdate
from src.models import Cart, Product, Service

router = APIRouter(
    prefix="/carts",
    tags=["cart"]
)


@router.get("/count")
def get_cart_count(new_db: Session = Depends(get_session)):
    return CartService.get_count(db = new_db)


@router.get("/all")
def get_all_cart(newdb: Session = Depends(get_session)):
    return CartService.get_all(db = newdb)


@router.post("/add")
def add_cart(create_cart: CartCreate, new_db: Session = Depends(get_session)):

    return CartService.add_cart(new_cart=create_cart,db=new_db)


@router.put("/update")
def update_cart(oldname: str, newcart: CartUpdate,new_db: Session = Depends(get_session)):
    return CartService.update_cart(old_name=oldname,new_cart=newcart,db=new_db)


@router.delete("/delete")
def deletete_cart(oldname: str, new_db: Session = Depends(get_session)):
    return CartService.delete_cart(old_name=oldname,db=new_db)



@router.post("/sum")
def update_sum (cart_id,new_db: Session = Depends(get_session)):
    return CartService.calculate_cart_cost(cartid=cart_id,db = new_db)


