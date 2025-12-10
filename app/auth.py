from flask import Blueprint, request, render_template, redirect, url_for, session
from .models import User
from . import db

auth_bp = Blueprint("auth", __name__)

# Vulnerable login: plaintext password check + insecure dynamic filter
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # vulnerable: dynamic filter and plaintext comparison
        user = User.query.filter(f"username = '{username}'").first()
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for("todo.todos"))
    return render_template("login.html")

