from flask import Flask,render_template
import os

app = Flask(__name__)
BASEDIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template('home.html',name='andy')

if __name__ == "__main__":
    app.run(debug=True)