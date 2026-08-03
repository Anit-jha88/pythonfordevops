from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dummy Database
users = []

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Welcome to FastAPI"
    }

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def create_user(user: User):
    users.append(user.dict())
    return {
        "message": "User Added Successfully",
        "data": user
    }

@app.get("/users/{id}")
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    return {"message": "User Not Found"}

@app.put("/users/{id}")
def update_user(id: int, updated_user: User):
    for index, user in enumerate(users):
        if user["id"] == id:
            users[index] = updated_user.dict()
            return {
                "message": "Updated Successfully",
                "data": updated_user
            }
    return {"message": "User Not Found"}

@app.delete("/users/{id}")
def delete_user(id: int):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return {"message": "Deleted Successfully"}
    return {"message": "User Not Found"}