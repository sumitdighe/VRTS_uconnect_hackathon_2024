from sqlalchemy import Unicode
from sqlalchemy.orm import Session
from sqlalchemy.sql import compiler
from psycopg2.extensions import adapt as sqlescape
# or use the appropiate escape function from your db driver
from . import models, schemas


def get_user(db: Session, user_id: int):

    query=db.query(models.User)
    print(compile_query(query))
    return query.filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    query=db.add(db_user)
    print(compile_query(query))
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def compile_query(query):
    dialect = query.session.bind.dialect
    print(dialect)
    statement = query.statement
    print(statement)
    comp = compiler.SQLCompiler(dialect, statement)
    comp.compile()
    enc = dialect.encoding
    params = {}
    for k,v in comp.params.iteritems():
        if isinstance(v, Unicode):
            v = v.encode(enc)
        params[k] = sqlescape(v)
    return (comp.string.encode(enc) % params).decode(enc)