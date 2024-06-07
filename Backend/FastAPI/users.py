from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI()

#Entity user

class User(BaseModel):
    id: int
    name:str
    lastname: str
    Team: str
    age: int


users_list =[User(id=1,name="Franco", lastname="Rizzi",Team="BocaJuniors",age=27),
             User(id=2,name="Rizzi",lastname="Franco",Team="Bokee",age=30),
             User(id=3,name="Franco", lastname="Zingaretti",Team="CABJ",age=25)]
@app.get ("/usersjson")
async def usersjson():
    return [{"name": "Franco", "lastname": "Rizzi", "Team": "BocaJuniors", "age": 27},
            {"name": "Rizzi", "lastname": "Franco", "Team": "Bokee", "age":30},
            {"name": "Franco", "lastname": "Zingaretti", "Team": "CABJ", "age":25}]

@app.get ("/users")
async def users():
    return users_list

@app.get ("/user/{id}")
async def user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list (users)[0]
    except:
        return {"error":"user not found"}