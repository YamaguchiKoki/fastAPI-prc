from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import database, schemas, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter(
    prefix = '/user',
    tags=['users']
)
get_db = database.get_db


# passlib, bcryptをインストール
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post('/', response_model=schemas.ShowUser, )
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    hashedpassword = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.ShowUser, )
def get_user(id: int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPExecption(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"該当するユーザーが見つかりませんでした id={id}")
    return user