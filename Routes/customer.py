from  fastapi import APIRouter , status
from Database.db import connection
from Database.querys import queries
import pandas 
router=APIRouter(prefix="/customers",tags=["customers"],responses={status.HTTP_404_NOT_FOUND:{"message":"Not found"}})
@router.get("/",status_code=status.HTTP_200_OK)
async def customers():
    data=pandas.read_sql(queries["get_customers"],connection)
    return data.to_dict("records")
@router.post("/",status_code=status.HTTP_200_OK)
async def customers():
    data=pandas.read_sql(queries["get_customers"],connection)
    return data.to_dict("records")
     