# web_flask/flaskapp

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'
# this is a comment to test if jenkins will build and deploy after github push

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
