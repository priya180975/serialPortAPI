#datatype/object 
from pydantic import BaseModel 
from typing import Optional

class Users(BaseModel):
    username:str
    email:str
    password:str

class DisplayUser(BaseModel):
    username:str
    email:str
    class Config:
        orm_mode=True

# class updateUser(BaseModel):
#     password:str


class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None


class WeightData(BaseModel):
    weight:int
