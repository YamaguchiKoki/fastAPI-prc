from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = '/blog',
    tags=['blogs']
)
get_db = database.get_db


#  コレクションに対してパイデンティックスキーマを適用したいならList
@router.get('/', response_model=List[schemas.ShowBlog], )
def all (db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# document httpresponse読む
@router.post('/', status_code=status.HTTP_201_CREATED, )  
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, )
def update(id,request: schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"該当するブログが見つかりませんでした id={id}")
        blog.update(request)
        db.commit()
    return 'done'
        

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, )
def delete(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, )
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"該当するブログが見つかりませんでした id={id}")
    return blog