from flask import Flask, render_template, request
from ml import generate_model, web_scrape
import json
app = Flask(__name__)


@app.route('/')
def home():
    # all_goals = [
    #     'Server Migration',
    #     'Sales Tracking',
    #     'Customer Database',
    #     'Payout Details',
    #     'Account Setup',
    # ]
    # all_ratings = ['10', '20', '30', '40', '100']
    all_goals, all_ratings = generate_model()
    all_ratings = [str((int(a)/20)*100) for a in all_ratings]
    all_links = []
    # all_links = [web_scrape(a, 5) for a in all_goals]
    data = [0, 1000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 40000]
    data = [str(a) for a in data]
    data = ' '.join(data)
    return render_template("index.html", goals=all_goals, ids=all_ratings, links=all_links, server_data=data)


@app.route('/blank')
def blank():
    return render_template("blank.html")


@app.route('/NotFound')
def not_found():
    return render_template("404.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        fname = request.form["Fname"]
        lname = request.form["Lname"]
        first_goal = request.form["Fgoal"]
        second_goal = request.form["Sgoal"]

    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/buttons')
def buttons():
    return render_template("buttons.html")


@app.route('/cards')
def cards():
    return render_template("cards.html")


@app.route('/charts')
def charts():
    return render_template("charts.html")


@app.route('/tables')
def tables():
    return render_template("tables.html")


@app.route('/ForgotPassword')
def forgot_password():
    return render_template("forgot-password.html")


@app.route('/colors')
def colors():
    return render_template("utilities-color.html")


@app.route('/animation')
def animation():
    return render_template("utilities-animation.html")


@app.route('/border')
def border():
    return render_template("utilities-border.html")


@app.route('/other')
def other():
    return render_template("utilities-other.html")


if __name__ == "__main__":
    app.run(debug=True)
