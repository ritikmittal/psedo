import os
import smtplib
from flask import Flask, redirect, render_template, request

app= Flask(__name__)

students= []

@app.route("/")
def index():
    # UserAgent = request.user_agent.string
    return render_template("index.html",User =os.getenv('USER'))

@app.route("/registerents")
def registerents():
    return render_template("registered.html",students=students)

@app.route("/register",methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    comlplaint = request.form.get("comlplaint")
    if not name or not comlplaint or not email:
        return render_template("failure.html")
    # message="you are registered !!!"
    # server = smtplib.SMTP("smtp.gmail.com",587)
    # server.starttls()
    # server.login("mittalritik365@gmail.com","mnittpdtahu")
    # server.sendmail("mittalritik365", email , massage)
    students.append(f"{name} has a comlplaint : {comlplaint}")
    return redirect("/registerents")
