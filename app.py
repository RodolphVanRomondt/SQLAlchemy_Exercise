"""Blogly application."""

from flask import Flask, request, render_template,  redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
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
    tags = Tag.query.all()

    return render_template("post_form.html", user=user, tags=tags)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def post_post(user_id):

    title = request.form["title"]
    content = request.form["content"]

    post = Post(title=title, content=content, user_id=user_id)
    
    db.session.add(post)
    db.session.commit()

    for ele in list(request.form)[2:]:
        tag = Tag.query.filter(Tag.name == ele).one()
        
        p_t = PostTag(post_id=post.id, tag_id=tag.id)

        db.session.add(p_t)
    
    db.session.commit()

    return redirect(f"/users/{ user_id }")

@app.route("/posts/<int:post_id>")
def post_details(post_id):

    post = Post.query.get(post_id)
    tags = post.tagged

    return render_template("post_details.html", user=post.user, post=post, tags=tags)

@app.route("/posts/<int:post_id>/edit")
def post_edit(post_id):

    post = Post.query.get(post_id)
    tags = Tag.query.all()

    return render_template("post_edit.html", post=post, tags=tags)

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def post_edit_post(post_id):

    post = Post.query.get(post_id)
    post.title = request.form["title"]
    post.content = request.form["content"]

    tag_list = list(request.form)[2:]

    PostTag.query.filter(PostTag.post_id == post_id).delete()

    for ele in tag_list:

        tag = Tag.query.filter(Tag.name == ele).one()
        p_t = PostTag(post_id=post_id, tag_id=tag.id)

        db.session.add(p_t)
        db.session.commit()

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")

@app.route("/posts/<int:post_id>/delete")
def post_delete(post_id):

    post = Post.query.get(post_id)

    PostTag.query.filter(PostTag.post_id == post_id).delete()
    Post.delete_post(post_id)

    db.session.commit()

    return redirect(f"/users/{post.user_id}")

@app.route("/tags")
def tags_route():

    tags = Tag.query.all()

    return render_template("tags.html", tags=tags)

@app.route("/tags/new")
def tag_new():

    return render_template("tag_form.html")

@app.route("/tags/new", methods=["POST"])
def tag_post():

    name = request.form["name"]
    tag = Tag(name=name)
    
    db.session.add(tag)
    db.session.commit()

    return redirect("/tags")

@app.route("/tags/<int:tag_id>")
def tag_details(tag_id):

    tag = Tag.query.get(tag_id)

    return render_template("tag_details.html", tag=tag)

@app.route("/tags/<int:tag_id>/edit")
def tag_edit(tag_id):

    tag = Tag.query.get(tag_id)

    return render_template("tag_edit.html", tag=tag)

@app.route("/tags/<int:tag_id>/edit", methods=["POST"])
def tag_edit_post(tag_id):

    tag = Tag.query.get(tag_id)
    tag.name = request.form["name"]

    db.session.commit()

    return redirect(f"/tags/{tag.id}")

@app.route("/tags/<int:tag_id>/delete")
def tag_delete(tag_id):

    PostTag.query.filter(PostTag.tag_id == tag_id).delete()
    Tag.delete_tag(tag_id)

    db.session.commit()

    return redirect("/tags")