from flask import Flask, render_template

site = Flask(__name__)

@site.route("/")
def home():
    return render_template("login.html")

site.run(host="0.0.0.0", port=5000, debug=True)