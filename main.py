from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'My first flask app'

if __name__=='__main__':
    app.run()