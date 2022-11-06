from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)

@auth.route("/about")
def about():
    return render_template("about.html")

@auth.route("/contact")
def contact():
    return render_template("contact.html")

@auth.route("/login")
def Login():
    return render_template("login.html")

@auth.route("/sign-up")
def sign_up():
    return render_template("signup.html")

@auth.route("/sign-out")
def sign_out():
    return redirect(url_for("views.home"))