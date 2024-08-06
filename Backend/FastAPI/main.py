from fastapi import FastAPI
from routers import products


app = FastAPI()

#routers
app.include_router(products.router)




@app.get("/")
async def root():
    return "Hello FastAPI"

@app.get("/url")
async def url():
    return {"BOKA":"La 3era Suda es mi obsesion"}
