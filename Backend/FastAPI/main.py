from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Bocaaaaaaa"

@app.get("/url")
async def url():
    return {"BOKA":"La 3era Suda es mi obsesion"}
