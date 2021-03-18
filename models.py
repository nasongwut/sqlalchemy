from sqlalchemy import Column,create_engine,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birthday = Column(String)
    tel = Column(String)
    address = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=True)

class Drone(Base):
    __tablename__='drones'
    id = Column(Integer, primary_key=True, index=True)
    nbtc_id = Column(String)
    drone_name = Column(String)
    drone_model = Column(String)
    drone_brand = Column(String)
    drone_version = Column(String)
    insurance_id = Column(String)

# Create Database
# Base.metadata.create_all(engine)
    


    # items = relationship("Item", back_populates="owner")

