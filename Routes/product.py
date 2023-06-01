from fastapi import APIRouter ,status  ,Depends ,HTTPException
from Database.db import engine
from Database.querys import queries
import pandas 
router = APIRouter(prefix="/products",tags=["products"],responses={status.HTTP_404_NOT_FOUND:{"message":"Not found"}})
@router.get("/")
async def products():
    data = pandas.read_sql(queries["get_products"],engine)
    return data.to_dict("records")
@router.get("/{idProducto}")
async def product(idProducto):
    try:
       data = pandas.read_sql(queries["get_product"],engine,params=[idProducto])
       return data.to_dict("records")[0]
    except:
        raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,detail="Product Not found") 
@router.delete("/{idProducto}")
async def product(idProducto):
    pandas.read_sql(queries["delete_product"],engine,params=[idProducto])
    return {"ok"}






    




