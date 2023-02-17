from pydantic import BaseModel


class BodyPost(BaseModel):
    userId: int
    title: str
    body: str


class User(BaseModel):
    name: str
    job: str


class NewUser(BaseModel):
    email: str = "eve.holt@reqres.in"
    password: str = "pistolx"


# class BodyComment(BaseModel):
