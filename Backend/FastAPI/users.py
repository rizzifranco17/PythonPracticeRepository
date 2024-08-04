from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

#uvicorn users:app --reload --> TO Run
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
             User(id=3,name="Franco", lastname="Zingaretti",Team="CABJ",age=25),
             User(id=4,name="Franco", lastname="Zingaretti",Team="CABJ",age=25)]
@app.get ("/usersjson")
async def usersjson():
    return [{"name": "Franco", "lastname": "Rizzi", "Team": "BocaJuniors", "age": 27},
            {"name": "Rizzi", "lastname": "Franco", "Team": "Bokee", "age":30},
            {"name": "Franco", "lastname": "Zingaretti", "Team": "CABJ", "age":25}]

@app.get ("/user/")
async def users():
    return users_list

@app.get ("/user/{id}") #path
async def user(id:int):
    return search_user (id)
    
    
@app.get ("/userquery/") #query
async def user(id:int):
    return search_user (id)

@app.post("/user/", status_code=201)
async def user(user:User):
    if type (search_user(user.id))==User:
       raise HTTPException(status_code=404, detail="User already exist")
   
    users_list.append(user)
    
    return user



@app.put("/user/")
async def user(user: User):

    found = False
    print(user)

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error":"User not found"}
    else:
        return user


@app.delete("/user/{id}")
async def user(id:int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list [index]
            found = True

    if not found:
        return {"error":"user not found"}




def search_user(id:int):
    users = filter (lambda user: user.id == id, users_list)
    try:
        return list (users)[0]
    except:
        return {"error":"User not found"}
