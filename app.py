"""Blogly application."""

from flask import Flask, request, render_template,  redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "springboard"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

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

    return render_template("user_create.html")

@app.route("/users/<int:user_id>")
def add_route(user_id):

    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(Post.user_id == user_id).all()

    return render_template("user_details.html", user=user, posts=posts)

@app.route("/users/<int:user_id>/edit")
def edit_route(user_id):

    user = User.query.get(user_id)

    return render_template("user_edit.html", user=user)

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

    user = User.query.get(user_id)

    for post in user.posts:
        Post.delete_post(post.id)
    
    db.session.commit()

    User.delete_user(user_id)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:user_id>/posts/new")
def post_new(user_id):

    user = User.query.get(user_id)

    return render_template("post_form.html", user=user)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def post_post(user_id):

    title = request.form["title"]
    content = request.form["content"]

    post = Post(title=title, content=content, user_id=user_id)

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{ user_id }")

@app.route("/posts/<int:post_id>")
def post_details(post_id):

    post = Post.query.get(post_id)

    return render_template("post_details.html", user=post.user, post=post)

@app.route("/posts/<int:post_id>/edit")
def post_edit(post_id):

    post = Post.query.get(post_id)

    return render_template("post_edit.html", user=post.user, post=post)

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def post_edit_post(post_id):

    post = Post.query.get(post_id)

    post.title = request.form["title"]
    post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")

@app.route("/posts/<int:post_id>/delete")
def post_delete(post_id):

    post = Post.query.get(post_id)
    Post.delete_post(post_id)

    db.session.commit()

    return redirect(f"/users/{post.user_id}")