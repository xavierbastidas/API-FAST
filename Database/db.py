import pyodbc 
from dotenv import load_dotenv 
from os import environ
load_dotenv()
try:
    connection  = pyodbc.connect(environ.get('connection_string'))
    print("Successful Connection")
except Exception as ex:
    print(ex)


    







