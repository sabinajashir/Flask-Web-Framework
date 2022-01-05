from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/')
def index():
    return '<html><h1>Welcome to the home page.</h1></html>'

@app.route('/success/<int:score>')
def success(score):
    return 'The student passed with score : ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The student failed with score : ' + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 35:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run()