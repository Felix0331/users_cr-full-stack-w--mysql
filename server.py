from flask import Flask, render_template,request,redirect
from user import User
app = Flask(__name__)

@app.route("/users")
def index():

    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route("/users/new")
def add_user():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_friend():

    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }

    User.save(data)

    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)