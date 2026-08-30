# Fixture: Python file with FastAPI decorators
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/users")
def list_users():
    return [{"id": 1, "name": "Alice"}]


@app.get("/api/users/{user_id}")
def get_user(user_id: str):
    return {"id": user_id, "name": "Alice"}


@app.post("/api/users")
def create_user(data: dict):
    return {"id": 2, **data}


@app.delete("/api/users/{user_id}")
def delete_user(user_id: str):
    return {"deleted": user_id}
