from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Tests for model for Users and Posts."""

    def setUp(self):
        """Clean up any existing users and posts."""

        User.query.delete()
        Post.query.delete()

        user = User(first_name="TestUser", last_name="Springboard", image_url="www.google.com")
        db.session.add(user)
        db.session.commit()

        post = Post(title="First Post", content="Oh, hai.", user_id=1)
        db.session.add(post)
        db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_get_user(self):
        """ Get the user and compare its __repr__() """

        test_user = User.query.get(1)
        self.assertEqual(test_user, "<User: 1 First Name: TestUser Last Name: Springboard URL: www.google.com>")
    
    def test_get_post(self):
        """ Get the post and compare its __repr__() """

        test_post = Post.query.get(1)
        self.assertEqual(test_post, "<Post: 1 Title: First Post! UserID: 1>")
