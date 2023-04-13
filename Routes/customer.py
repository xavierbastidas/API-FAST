from  fastapi import APIRouter , status,Body
from Database.db import connection
from Database.querys import queries
import datetime
import pandas 
router=APIRouter(prefix="/customers",tags=["customers"],responses={status.HTTP_404_NOT_FOUND:{"message":"Not found"}})
@router.get("/",status_code=status.HTTP_200_OK)
async def customers():
    data=pandas.read_sql(queries["get_customers"],connection)
    return data.to_dict("records")
@router.post("/")
async def customers(nombre:str= Body(...),cedula:str=Body(...),
                    correo:str=Body(...),telefono:str=Body(...),fechaRegistro:datetime=Body(...)):
    data=pandas.read_sql(queries["add_new_customer"],connection,params=[nombre,cedula,correo,telefono,fechaRegistro])
    return data.to_dict("records")
    
     