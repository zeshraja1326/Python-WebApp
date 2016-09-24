import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgres://username:password@server:5432/database' #CHANGE IT TO YOURS!
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
