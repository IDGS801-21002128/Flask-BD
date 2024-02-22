import os
from sqlalchemy import create_engine

import urllib

class Config(objetc):
    SECRET_KEY = "Clave secreta"
    SESSION_COOKIE_SECURE=False

class DevelomentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URL="MYSQL+PYMYSQL://root:root@127.0.0.1/bdiddgs801"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
