import pymysql
import os


dbusername = 'mysql+pymysql://PasContent_CDA:'
userpath = 'XxP@rDefau!txX@'
basedir = 'da.cefim-formation.org'
dbname = '/PasContent_CDA'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = dbusername + userpath + basedir +dbname
    SQLALCHEMY_TRACK_MODIFICATIONS = False