#####################
## Depency imports ##
#####################
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

############
## Config ##
############
app = Flask(__name__) #Don't change it, this is default
app.config.from_object('config') #config file import
app.secret_key = 'Application_Key' #KEEP IT IN SECRET!

CORS(app) #Enable CORS Support to allow Clients to work with your API
db = SQLAlchemy(app) #Import Database


#################
## App imports ##
#################
from app import models, controllers #Import in-App depencies