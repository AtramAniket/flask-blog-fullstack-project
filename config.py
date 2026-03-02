import os
from dotenv import load_dotenv

load_dotenv()

class Config:

	SECRET_KET = os.getenv("APP_SECRET_KEY")

	SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")