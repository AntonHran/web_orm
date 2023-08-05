from configparser import ConfigParser
from pathlib import Path

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

config_path = Path(__file__).parent.parent.joinpath('config_7_1.ini')
# print(config_path)
parser = ConfigParser()
parser.read(config_path)

user = parser.get('DB', 'user')
password = parser.get('DB', 'password')
db_name = parser.get('DB', 'db_name')
domain = parser.get('DB', 'domain')
port = parser.get('DB', 'port')

url = f'postgresql://{user}:{password}@{domain}:{port}/{db_name}'

engine = create_engine(url, echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()
