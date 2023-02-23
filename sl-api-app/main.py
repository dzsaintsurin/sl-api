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
    title="SalesLoft TechOps Exercise!",
    version=1.0,
    description="SL-API",
    docs_url="/",
    contact=contact,
)


@app.get("/api/v1/resource", description="Return a list of available resources")
async def list_resource():
    return validate_response(get_resource())


@app.get("/api/v1/users", description="Give a list of the users in the current page")
async def list_users(page: int):
    return validate_response(get_resource(page))


@app.get("/api/v1/users/{userId}", description="This will get a user by Id")
async def single_user(userId: int):
    return validate_response(get_resource(userId))


@app.get(
    "/api/v1/resource/{resourceId}",
    description="Return a specific resource base on its Id",
)
async def single_resource(resourceId: int):
    return validate_response(get_resource(f"{resourceId}"))


@app.post("/api/v1/users", description="Create a new user")
async def create_users(user: User):
    user = user.dict()
    return validate_response(create_user(user))


@app.put("/api/v1/users/{userId}", description="Update an existing user attribut")
async def update_user(userId: int, user: User):
    user = user.dict()
    return validate_response(create_user(user, userId))


@app.patch("/api/v1/users/{userId}", description="Similar to Udate User")
async def patch_user(userId: int, user: User):
    user = user.dict()
    return validate_response(create_user(user, userId))


@app.delete("/api/v1/users/{userId}", description="Delete a user")
async def delete_user(userId: int):
    return validate_response(create_user(userId=userId))


@app.post(
    "/api/v1/register",
    description="Create a new user, Please Note: Only defined users succeed registration.",
)
async def register(user: NewUser):
    user = user.dict()
    return validate_response(create_user(user))


@app.post("/api/v1/login", description="A Fake login")
async def login(user: NewUser):
    user = user.dict()
    return validate_response(create_user(user))


def validate_response(response):
    if type(response) is tuple:
        raise HTTPException(status_code=response[0], detail=response[1])
    return response


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )
