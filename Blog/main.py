from fastapi import FastAPI
from . import models
from .database import engine
from .router import blog 
from .router import user 

app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(blog.router) 
app.include_router(user.router) 









