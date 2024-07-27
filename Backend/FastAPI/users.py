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
    return search_user (id)
    
    
@app.get ("/userquery/")
async def user(id:int):
    return search_user (id)

app.post("/user/")
async def user(user:User):
    if type (search_user(user.id))==User:
     return{"error":"User already exist"}
    else:
        users_list.append(user)

app.put("/user/")
async def user(user:User):

    Found = False

    for index,saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user

    if not Found:
        return {"error":"User not found"}


def search_user(id:int):
    users = filter (lambda user: user.id == id, users_list)
    try:
        return list (users)[0]
    except:
        return {"error":"User not found"}

