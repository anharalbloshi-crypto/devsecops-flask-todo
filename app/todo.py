from flask import Blueprint, request, render_template
from .models import Todo
from . import db

todo_bp = Blueprint("todo", __name__)

@todo_bp.route("/todos", methods=["GET", "POST"])
def todos():
    if request.method == "POST":
        text = request.form.get("text")
        new = Todo(text=text, user_id=1)
        db.session.add(new)
        db.session.commit()

    all_todos = Todo.query.all()
    return render_template("todos.html", todos=all_todos)
