from fastapi import APIRouter ,status  ,Depends ,HTTPException
from Database.db import connection
from Database.querys import queries
import pandas 
router = APIRouter(prefix="/products",tags=["products"],responses={status.HTTP_404_NOT_FOUND:{"message":"Not found"}})
@router.get("/")
async def products():
    data = pandas.read_sql(queries["get_products"],connection)
    return data.to_dict("records")
@router.get("/{idProducto}")
async def product(idProducto):
    try:
       data = pandas.read_sql(queries["get_product"],connection,params=[idProducto])
       return data.to_dict("records")[0]
    except:
        raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,detail="Product Not found") 
    
@router.delete("/{idProducto}",status_code=status.HTTP_204_NO_CONTENT)
async def product(idProducto):
    pandas.read_sql(queries["delete_product"],connection,params=[idProducto])



    




