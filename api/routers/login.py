# login to generate jwt

from fastapi import APIRouter,Depends,status,HTTPException
import schemas,models
from sqlalchemy.orm import Session
from database import get_db
from passlib.context import CryptContext
from datetime import timedelta,datetime
from jose import jwt,JWTError
from schemas import TokenData
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

SECRET_KEY='deda20cc011f5a74908b4123e0fed28a5350e0ff3f2ff4474cf3e4ca686f8dd0'
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=20

#jwt token 
def generate_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


router=APIRouter( 
    tags=['Login']
)

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")


@router.post('/login')
# def login(request:schemas.Login,db:Session=Depends(get_db)):
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    userdata=db.query(models.Users).filter(models.Users.username==request.username).first()
    if not userdata:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not found/invalid user")
    if not pwd_context.verify(request.password,userdata.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Password")
    
    access_token=generate_token(
        data={"sub":userdata.username}
    )
    return {"access_token":access_token,"token_type":"bearer"}


def get_current_user(token:str=Depends(oauth2_scheme)):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid auth credentials",
        headers={'WWW-Authenticate':'Bearer'}
    )
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data=TokenData(username=username)
    except JWTError:
        raise credentials_exception

