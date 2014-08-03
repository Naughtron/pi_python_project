# this is the initiation script 
from flask import Flask 

app = Flask(__name__)
# tell the __init__ that we are now using a config file
app.config.from_object('config')

from app import views 



