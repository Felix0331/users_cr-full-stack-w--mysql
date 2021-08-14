from flask import render_template,request,redirect
from flask_app import app

from flask_app.models.user import User


# Landing Page
@app.route("/users")
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

# Create Page
@app.route("/users/new")
def add_user():
    return render_template("create.html")

# Show Single User
@app.route("/users/<int:id>")
def display_user(id):
    data={
        "id":id
    }
    user = User.get_user(data)
    return render_template("user_read.html",single_user = user)

#Edit Page Render
@app.route('/users/<int:id>/edit')
def display_update(id):
    data={
        "id":id,
    }
    user = User.get_user(data)
    return render_template("user_edit.html",user = user)

#Update User
@app.route('/update_user/<int:id>', methods=["POST"])
def user_update(id):
    data = {
        "id":id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update_user(data)
    return redirect(f'/users/{id}')

# Method that creates single user
@app.route('/create_user', methods=["POST"])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    id = User.save(data)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/destroy')
def delete_user(id):
    data={
        "id":id,
    }
    User.user_delete(data)
    return redirect("/users")
