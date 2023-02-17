"""
Dael Saint-Surin
02/16/2023
"""

from pydantic import BaseModel


class User(BaseModel):
    name: str
    job: str


class NewUser(BaseModel):
    email: str = "eve.holt@reqres.in"
    password: str = "pistolx"
