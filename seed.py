"""Seed file to make sample data for users db."""

from models import User, db, Post, Tag, PostTag

# Create all tables

# clean reset the database
# db.engine.execute('DROP SCHEMA public CASCADE; CREATE SCHEMA public;')
# creates tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
dof = User(first_name='Rodolph', last_name="Van Romondt", image_url="https://lh3.googleusercontent.com/a/ACg8ocKCaB0i3DZctm3GL57I9ywQnnNe4nL_ix9mM8WBdubKIvE=s324-c-no")
colt = User(first_name='Colt', last_name="Steele", image_url="https://cdn.vectorstock.com/i/1000x1000/15/40/blank-profile-picture-image-holder-with-a-crown-vector-42411540.webp")
david = User(first_name='David', last_name="Adewole", image_url="https://images.unsplash.com/photo-1628563694622-5a76957fd09c?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

# Add new objects to session
db.session.add_all([dof, colt, david])

# Commit
db.session.commit()

# Add posts
post1 = Post(title='First Post!', content='Oh, hai.', user_id=1)
post2 = Post(title='Springboard', content='Software Engineering.', user_id=1)
post3 = Post(title='Second Post!', content='Oh, hai.', user_id=2)
post4 = Post(title='Third Post!', content='Oh, hai.', user_id=3)

# Add new objects to session
db.session.add_all([post1, post2, post3, post4])

# Add tags
tag1 = Tag(name='Fun')
tag2 = Tag(name='Cool')
tag3 = Tag(name='Perfect')

# Add new objects to session
db.session.add_all([tag1, tag2, tag3])

# Commit
db.session.commit()

# Add posts - tags relationship
pt1 = PostTag(post_id=1, tag_id=1)
pt2 = PostTag(post_id=1, tag_id=2)
pt3 = PostTag(post_id=2, tag_id=3)
pt4 = PostTag(post_id=3, tag_id=1)
pt5 = PostTag(post_id=3, tag_id=2)
pt6 = PostTag(post_id=3, tag_id=3)

# Add new objects to session
db.session.add_all([pt1, pt2, pt3, pt4, pt5, pt6])

# Commit
db.session.commit()