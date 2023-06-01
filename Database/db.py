
'''
import pyodbc 
import 
from dotenv import load_dotenv 
from os import environ
load_dotenv()
try:
   # connection  = pyodbc.connect("DRIVER={SQL Server};SERVER=XAVIER;DATABASE=Orden_Venta;UID=xavs;PWD=prueba123")
    print("Successful Connection")
except Exception as ex:
    print(ex)

'''
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker
server = 'XAVIER' 
database = 'Orden_Venta' 
username = 'xavs' 
password = 'prueba1234'
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+password+"")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
Base=declarative_base()
SessionLocal = sessionmaker(bind=engine)



    







