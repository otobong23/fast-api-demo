from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("Javascript23$")
db_url = f"postgresql://postgres:{password}@localhost:5432/fast_api_demo"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
