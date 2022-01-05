from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<html><h2>Using Flask Web Framework</h2></html>'

if __name__ == '__main__':
    app.run()