from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import models



# models.Base.metadata.create_all(engine)
def create_database(engine):
    models.Base.metadata.create_all(engine)



