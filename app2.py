#importing flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
#object is created for flask
app=Flask(__name__)

urls=[
{
	'id':1,
	's_path': 'abc',  #short url
	'l_url': 'https://www.facebook.com/'   #long url
}
]

#templates for HTMl
#static for CSS,JS files
# specify when to execute function
@app.route('/<string:url>')
def url_shorten(url):
	for single_url in urls:
		if url==single_url['s_path']:
			return redirect(single_url['l_url'])
	return 'hello world'
	


#run the server
if __name__ == '__main__':
	app.run(debug=True)