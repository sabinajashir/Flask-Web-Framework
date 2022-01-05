### Integrate HTML templates with flask
### HTTP GET and POST
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score >= 50 :
        res = 'PASSED'
    return render_template('results.html',results=res)

@app.route('/fail/<int:score>')
def fail(score):
    res=''
    if score < 50 :
        res = 'FAILED'
    return render_template('results.html',results=res)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 35:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))
###result checker html page with submit button
@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method =='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['Data_Science'])

        total_score=(science+maths+c+data_science)/4

    res =''
    if total_score>50 :
        res = 'success'
    else:
        res = 'fail'
    return redirect(url_for(res,score=total_score))
if __name__ == '__main__':
    app.run()