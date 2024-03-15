from fastapi import APIRouter
from pydantic import BaseModel, field_validator,root_validator

users = APIRouter()


class user(BaseModel):
    name: str = "peileon"
    age: int = 26
    
    @field_validator('name')
    def username_must_contain_underscore(cls, v):
        if '_' not in v:
            raise ValueError('username must contain an underscore')
        return v


@users.post("/items/{posst}")
async def read_items(user: user, posst: str = "NO_first"):
    return {"age": user.age, "posst": posst}
