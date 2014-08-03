# imports 
from flask import render_template, flash, redirect
from app import app
from forms import LoginForm 

# set the app route for login in module 3
@app.route('/login', methods = ['GET', 'POST']) # tells the app it can accecpt GET and POST
def login():
	form = LoginForm() 
	if form.validate_on_submit(): #reder the template before the user can enter data
		flash('Login requested for OpenId="' + form.openid.data + '", remember=' + str(form.remember_me.data))
		return redirect('/index') # if all the data is valid the user will re-direct to index. If not user will be asked to enter it again
	return render_template('login.html', title = 'Sign In', form = form, providers = app.config['OPENID_PROVIDERS']) # adding open ID array from config

# set the app routes for requests in module 1
@app.route('/')
@app.route('/index')
def index():
	return "Hello World!"

# set the app routes for requests in module 2
@app.route('/mod2')
# define what happens when we hit either of the above paths
def mod2():
	user = {'nickname': 'Naughtron'} # mock user
	# create some fake posts for the site
	posts = [
	{
	'author': {'nickname': 'Jeff'},
	'body': 'Be the bomb you throw!'

	}, 
	{ 
	'author': {'nickname': 'Connor'}, 
	'body': 'I am a real life lore nerd'

	}
]
	# return the html template I created app/templates
	return render_template("index.html", title = 'Home', user = user, posts = posts)
	# set the html template to: title 'Home' and Username to mock user