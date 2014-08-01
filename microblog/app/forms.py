'''Login Form'''
# imports 
from flask.ext.wtf import Form 
from wtforms import TextField, BooleanField # this is for the login and checkbox
from wtforms.validators import Required # this is the validator not submitted empty

# login Class
class LoginForm(Form):
	openid = TextField('openid', validators = [Required()]) # login
	remember_me = BooleanField('remember_me', default = False) # remember me checkbox

