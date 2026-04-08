from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env

# password = quote_plus("[password]")
# # quote_plus is a utility function in the urllib.parse module used for URL-encoding strings, specifically designed for query strings (the part of a URL after the ?). Was used on the password to encode it

db_url = os.getenv("DATABASE_URL") or ''

engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
