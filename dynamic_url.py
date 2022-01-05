from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><h1>Welcome to the home page.</h1></html>'

@app.route('/success/<int:score>')
def success(score):
    return 'The student passed with score : ' + str(score) +

@app.route('/fail/<int:score>')
def fail(score):
    return 'The student failed with score : ' + str(score)
if __name__ == '__main__':
    app.run()