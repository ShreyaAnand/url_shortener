#importing flask
from flask import Flask
from flask import render_template
from flask import request
#object is created for flask
app=Flask(__name__)

urls=[
{
	'id':1,
	's_url': 'abc',  #short url
	'l_url': 'www.facebook.com'   #long url
}
]

#templates for HTMl
#static for CSS,JS files
# specify when to execute function
@app.route('/home',methods=['GET','POST'])
def url_shorten():
	return render_template('home.html')


#run the server
if __name__ == '__main__':
	app.run(debug=True)