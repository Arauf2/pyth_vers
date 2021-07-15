# web_flask/flaskapp

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'pop smoke album tm you best bump it'
#this is a comment to test if jenkins will build w webhook trigger

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
