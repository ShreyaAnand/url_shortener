#importing flask
from flask import Flask
#object is created for flask
app=Flask(__name__)

#templates for HTMl
#static for CSS,JS files
# specify when to execute function
@app.route('/')
def hello_world():
	return 'hello world'

@app.route('/<string:user>')
def hello_user(user):
	return 'hello '+ user

#run the server
if __name__ == '__main__':
	app.run(debug=True)