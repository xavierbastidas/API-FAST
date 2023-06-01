from  fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from Routes import customer , product
origins = [
    "*"
]
app= FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                    allow_credentials=True,
                     allow_methods=["*"],
                    allow_headers=["*"],
                   )
app.include_router(customer.router)
app.include_router(product.router)
print("http://127.0.0.1:8000")
@app.get("/")
async def root():
  return {"message":"Hi wordl"}





  


