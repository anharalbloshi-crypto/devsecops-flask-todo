from flask import Blueprint, request, render_template, redirect, url_for
from .models import User
from . import db

auth_bp = Blueprint("auth", __name__)

# ثغرة SQL injection متعمدة
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        # ← لا يوجد أي حماية، استعلام مباشر
        user = User.query.filter(f"username = '{username}'").first()
        if user:
            return redirect(url_for("todo.todos"))
    return render_template("login.html")
