#route to users

from fastapi import APIRouter,status
import schemas,models
from sqlalchemy.orm import Session
from fastapi.params import Depends
from database import get_db
from typing import List
from passlib.context import CryptContext


router=APIRouter(
    tags=['Users'],
    prefix="/users"
)

pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')#hashing


#create 
@router.post('',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.Users,db:Session=Depends(get_db)):
    hashedpassword=pwd_context.hash(request.password)
    new_user=models.Users(username=request.username,email=request.email,password=hashedpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#get 
@router.get('',response_model=List[schemas.DisplayUser])
def get_users(db:Session=Depends(get_db)):
    users=db.query(models.Users).all()
    return users


#update
# @router.put('/{id}')
# def update_user(id,request:schemas.updateUser,db:Session=Depends(get_db)):
#     user=db.query(models.Users).filter(models.Users.id==id)
#     if not user.first():
#         pass
#     user.update(request.dict())
#     db.commit()
#     return f'User with id {user.id} updated successfully'