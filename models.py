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

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(20),
                     nullable=False)
    
    last_name = db.Column(db.String(20),
                     nullable=False)
    
    image_url = db.Column(db.String(70),
                     nullable=False)

    def __repr__(self):
        """Show info about user."""

        p = self
        return f"<User: {p.id} First Name: {p.first_name} Last Name: {p.last_name} URL: {p.image_url}>"

    @classmethod
    def delete_user(cls, user_id):
        """Delete a User."""

        return cls.query.filter(User.id == user_id).delete()
