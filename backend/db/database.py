from typing import Annotated
from fastapi import Depends, HTTPException
from sqlmodel import SQLModel, Session, create_engine, select

from backend.utils.configs import get_db_url
from backend.models import *

engine = create_engine(url=get_db_url(), 
                       echo=False, 
                       connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
        yield session

class Database:

    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, _session):
        self.__session = _session

    def create_db_obj(
            self,
            db_cls: SQLModel, 
            req_obj: SQLModel, 
            extra_params:dict={}
            ):
        db_obj = db_cls.model_validate(req_obj, update=extra_params)
        return db_obj
        
    def create(self, 
            db_cls: SQLModel, 
            req_obj: SQLModel, 
            extra_params:dict={}):
        db_obj = self.create_db_obj(db_cls, req_obj, extra_params)
        db_obj = self.save(db_obj)
        return db_obj
    
    def update(self,
               db_cls: SQLModel, 
               db_id: int,
               req_obj: SQLModel, 
               extra_params:dict={}):
        db_obj = self.fetch_one(db_cls, db_id)
        req_data = req_obj.model_dump(exclude_unset=True)
        db_obj.sqlmodel_update(req_data, update=extra_params)
        db_obj = self.save(db_obj)
        return db_obj
    
    def delete(self, 
               db_cls:SQLModel, id):
        db_obj = self.fetch_one(db_cls, id)
        self.session.delete(db_obj)
        self.session.commit()

    def fetch(self, 
              db_cls: SQLModel,*, offset, limit):
        stmt = select(db_cls)
        stmt = stmt.offset(offset)
        stmt = stmt.limit(limit)
        results = self.session.exec(stmt).all()
        
        return results
    
    def fetch_one(self, 
                  db_cls: SQLModel, 
                  db_id: int
                  ):
        db_obj = self.session.get(db_cls, db_id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Resource not found")
        return db_obj
    
    def save(self, db_obj: SQLModel):
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj
    

def get_db(db: Annotated[Database, Depends(Database)], session: Annotated[Session, Depends(get_session)]):
    db.session = session
    yield db

def create_db_tables():
    SQLModel.metadata.create_all(engine)

def drop_db_tables():
    pass
    # SQLModel.metadata.drop_all(engine)