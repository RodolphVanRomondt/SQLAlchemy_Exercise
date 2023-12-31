"""Seed file to make sample data for users db."""

from models import User, db, Post
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
dof = User(first_name='Rodolph', last_name="Van Romondt", image_url="https://lh3.googleusercontent.com/a/ACg8ocKCaB0i3DZctm3GL57I9ywQnnNe4nL_ix9mM8WBdubKIvE=s324-c-no")
colt = User(first_name='Colt', last_name="Steele", image_url="www.google.com")
david = User(first_name='David', last_name="Adewole", image_url="www.google.com")

# Add new objects to session, so they'll persist
db.session.add(dof)
db.session.add(colt)
db.session.add(david)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add posts
post1 = Post(title='First Post!', content='Oh, hai.', user_id=1)
post2 = Post(title='Springboard', content='Software Engineering.', user_id=1)
post3 = Post(title='Second Post!', content='Oh, hai.', user_id=2)
post4 = Post(title='Third Post!', content='Oh, hai.', user_id=3)