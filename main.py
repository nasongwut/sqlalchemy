
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker
from database import create_database
from models import Drone

engine = create_engine('sqlite:///database.db')
create_database(engine)

obj_session = sessionmaker(engine)
session = obj_session()

data = Drone(id=1,nbtc_id="11005",drone_name="SongwutDrone",drone_model="tic-drone-v1",drone_brand="Thai Inovation",drone_version="v1",insurance_id="1201201")
session.add(data)
session.commit()




