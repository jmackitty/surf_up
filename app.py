from pickle import TRUE
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'


#set FLASK_APP=app.py

#export FLASK_ENV=development

#debug=TRUE

# export FLASK_DEBUG=0