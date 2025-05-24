from flask import Blueprint, render_template, redirect, url_for

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("base.html")

@main_bp.route("/dashboard")
def dashboard():
    return "Добро пожаловать!"
