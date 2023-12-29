"""Blogly application."""

from flask import Flask, request, render_template,  redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SECRET_KEY'] = "springboard"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_route():

    return redirect("/users")

@app.route("/users")
def users_route():
    """ Show the list of users page """

    users = User.query.all()

    return render_template("users.html", users=users)

@app.route("/users/new", methods=["POST"])
def users_redirect():

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.route("/users/new")
def create_route():
    """ Show create new user page """

    return render_template("create.html")

@app.route("/users/<int:user_id>")
def add_route(user_id):

    user = User.query.get_or_404(user_id)

    return render_template("details.html", user=user)

@app.route("/users/<int:user_id>/edit")
def edit_route(user_id):

    user = User.query.get(user_id)

    return render_template("edit.html", user=user)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edited_route(user_id):

    user = User.query.get(user_id)

    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<user_id>/delete")
def delete_user(user_id):

    User.delete_user(user_id)
    db.session.commit()

    return redirect("/users")