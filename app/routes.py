
from app import app
from flask import Flask, render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/name",defaults={'name' :"Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"

@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/k1")
def book1():
    return render_template('k1.html')

@app.route("/k2")
def book2():
    return render_template('k2.html')

@app.route("/k3")
def book3():
    return render_template('k3.html')

@app.route("/k4")
def book4():
    return render_template('k4.html')

@app.route("/k5")
def book5():
    return render_template('k5.html')

@app.route("/k6")
def book6():
    return render_template('k6.html')

@app.route("/k7")
def book7():
    return render_template('k7.html')

@app.route("/k8")
def book8():
    return render_template('k8.html')

@app.route("/k9")
def book9():
    return render_template('k9.html')

@app.route("/k10")
def book10():
    return render_template('k10.html')

@app.route("/k11")
def book11():
    return render_template('k11.html')

@app.route("/k12")
def book12():
    return render_template('k12.html')

