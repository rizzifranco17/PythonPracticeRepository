from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI()

#Entity user

class User(BaseModel):
    name:str
    lastname: str
    Team: str
    age: int


users_list =[User(name="Franco", lastname="Rizzi",team="BocaJuniors",age=27)
        User(name="Rizzi",lastname="Franco",team="Bokee",age=30)
        User(name="Franco", lastname="Zingaretti",team="CABJ",age=25)]
@app.get ("/usersjson")
async def users():
    return [{"name": "Franco", "lastname": "Rizzi", "Team": "BocaJuniors", "age": 27},
            {"name": "Rizzi", "lastname": "Franco", "Team": "Bokee", "age":30},
            {"name": "Franco", "lastname": "Zingaretti", "Team": "CABJ", "age":25}]

@app.get ("/users")
async def users():
    return users_list