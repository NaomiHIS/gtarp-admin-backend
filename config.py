import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///laws.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TELEGRAM_BOT_TOKEN = os.getenv('TELEG5788306619:AAEhU9vHWyCzWOjtv_hBgDqY0f9pCKiYyo4')
    TELEGRAM_LOGIN_REDIRECT_URL = os.getenv('TELEGRAM_LOGIN_REDIRECT_URL', 'http://localhost:5000/telegram-login')