# imports 
from flask import render_template
from app import app

# set the app routes for requests in module 1
@app.route('/')
@app.route('/index')
def index():
	return "Hello Wolrd!"

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