from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Tests for model for Users."""

    def setUp(self):
        """Clean up any existing users."""

        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_get_user(self):

        user = User(first_name="TestUser", last_name="Springboard", image_url="www.google.com")
        db.session.add(user)
        db.session.commit()

        test_user = User.query.get(1)
        self.assertEqual(test_user, "<User: 1 First Name: TestUser Last Name: Springboard URL: www.google.com>")

