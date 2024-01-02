"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(70), nullable=False)

    posts = db.relationship("Post")

    def __repr__(self):
        """Show info about user."""

        p = self
        return f"<User: {p.id} First Name: {p.first_name} Last Name: {p.last_name} URL: {p.image_url}>"

    @classmethod
    def delete_user(cls, user_id):
        """Delete a User."""

        return cls.query.filter(User.id == user_id).delete()
    
class Post(db.Model):
    """ Post. """

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User")
    tags = db.relationship("Tag", secondary="posts_tags", backref="posts")

    def __repr__(self):
        """ Show info about post """

        p = self
        return f"<Post: {p.id} Title: {p.title} UserID: {p.user_id}>"
    
    @classmethod
    def delete_post(cls, post_id):
        """Delete a Post."""

        return cls.query.filter(Post.id == post_id).delete()
    
class Tag(db.Model):

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)

    def __repr__(self):
        """Show info about user."""

        p = self
        return f"<Post: {p.id} First Name: {p.name}>"
    
    @classmethod
    def delete_tag(cls, tag_id):
        """Delete a Post."""

        return cls.query.filter(Tag.id == tag_id).delete()
    
class PostTag(db.Model):

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True)

    posts = db.relationship("Post", backref="tagged")
    tags = db.relationship("Tag", backref="posted")
