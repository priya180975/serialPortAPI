from fastapi import FastAPI
import models #database structure
# from database import engine #db configuration
# from routers import users,login,weightdata

app=FastAPI()

# app.include_router(users.router)
# app.include_router(login.router)
# app.include_router(weightdata.router)

@app.get('/')
def main_page():
    return 'Hi'

@app.get('/newpath')
def new_path():
    return {'Data':['1','2'],'New':'Priya'}

#convert models to db table
# models.Base.metadata.create_all(engine)