from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/blank')
def blank():
    return render_template("blank.html")


@app.route('/NotFound')
def not_found():
    return render_template("404.html")


@app.route('/login')
def login():
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
