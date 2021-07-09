import os

from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BASEDIR = Path().resolve()

class BaseConfig:
    """Base configuration"""
    # Set Flask config variables
    SECRET_KEY = os.getenv('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False