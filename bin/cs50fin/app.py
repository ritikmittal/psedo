from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # fecth from data
        userDetails = request.form
        id = userDetails['id']
        passwd = userDetails['passwd']
        return render_template('index.html')
