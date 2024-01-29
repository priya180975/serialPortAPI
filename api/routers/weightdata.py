#route to weighbridge

from fastapi import APIRouter,status
import schemas,models
from sqlalchemy.orm import Session
from fastapi.params import Depends
from database import get_db
from typing import List
from .login import get_current_user


router=APIRouter(
    tags=['WeightData'],
    prefix="/weightdata"
)


#read
@router.get('',response_model=List[schemas.WeightData])
def get_weightData(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    weightdatas=db.query(models.WeightData).all()
    return weightdatas

#update
@router.put('')
def create_weightData(request:schemas.WeightData,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    current_weightData=db.query(models.WeightData).filter(models.WeightData.id==1)
    if not current_weightData.first():
        print("In here")
        new_weightData=models.WeightData(weight=request.weight)
        db.add(new_weightData)
        db.commit()
        db.refresh(new_weightData)
        return 'Create and Update success'
    current_weightData.update(request.dict())
    db.commit()
    return 'Update success'


# #create
# @router.post('',status_code=status.HTTP_201_CREATED)
# def create_weightData(request:schemas.WeightData,db:Session=Depends(get_db)):
#     new_weightData=models.WeightData(weight=request.weight)
#     db.add(new_weightData)
#     db.commit()
#     db.refresh(new_weightData)
#     return new_weightData