"""
Dael Saint-Surin
02/16/2023
"""
import uvicorn

from fastapi import FastAPI, HTTPException
from models import User, NewUser
from reqres_api import get_resource
from reqres_api import create_user

contact = {"Name": "Dael Saint-Surin", "Email": "dzsaintsurin@protonmail.com"}

app = FastAPI(
    title="SL-API",
    version=1.0,
    description="Salesloft TechOps Exercise",
    docs_url="/",
    contact=contact,
)


@app.get("/api/v1/resource", description="Return a list of available resources")
def list_resource():
    return get_resource()


@app.get("/api/vi/users", description="Give a list of the users in the current page")
async def list_users(page: int):
    return get_resource(page)


@app.get("/api/vi/users/{userId}", description="This will get a user by Id")
async def single_user(userId: int):
    return get_resource(userId)


@app.get(
    "/api/v1/resource/{resourceId}",
    description="Return a specific resource base on its Id",
)
def single_resource(resourceId: int):
    response = get_resource(f"{resourceId}")
    return validate_response(response)


@app.post("/api/vi/users", description="Create a new user")
async def create_users(user: User):
    user = user.dict()
    response = create_user(user)
    return validate_response(response)


@app.put("/api/vi/users/{userId}", description="Update an existing user attribut")
async def update_user(userId: int, user: User):
    user = user.dict()
    response = create_user(user, userId)
    return validate_response(response)


@app.patch("/api/vi/users/{userId}", description="Similar to Udate User")
async def patch_user(userId: int, user: User):
    user = user.dict()
    response = create_user(user, userId)
    return validate_response(response)


@app.delete("/api/vi/users/{userId}", description="Delete a user")
async def delete_user(userId: int):
    response = create_user(userId=userId)
    return validate_response(response)


@app.post(
    "/api/vi/register",
    description="Create a new user, Please Note: Only defined users succeed registration.",
)
async def register(user: NewUser):
    user = user.dict()
    response = create_user(user)
    return validate_response(response)


@app.post("/api/v1/login", description="A Fake login")
async def login(user: NewUser):
    user = user.dict()
    response = create_user(user)
    return validate_response(response)


def validate_response(response):
    if type(response) is tuple:
        raise HTTPException(status_code=response[0], detail=response[1])
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
