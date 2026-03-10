import os
from dotenv import load_dotenv

load_dotenv()

class Config:

	SECRET_KEY = os.getenv("APP_SECRET_KEY")

	SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

	BOOTSTRAP_BOOTSWATCH_THEME = "brite"