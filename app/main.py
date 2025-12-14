from fastapi import FastAPI
from models import User
from database import users_collection, cursor, conn

app = FastAPI()

@app.post("/users")
def create_user(user: User):
    users_collection.insert_one(user.dict())
    cursor.execute("INSERT INTO logs (action) VALUES (?)", ("User created",))
    conn.commit()
    return {"message": "User created"}

@app.get("/users")
def get_users():
    users = list(users_collection.find({}, {"_id": 0}))
    return users

