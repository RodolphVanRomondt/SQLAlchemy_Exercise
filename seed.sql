-- from the terminal run:
-- psql < seed.sql

DROP DATABASE IF EXISTS blogly;

CREATE DATABASE blogly;

\c blogly

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  image_url TEXT NOT NULL
);

INSERT INTO users (first_name, last_name, image_url)
VALUES
  ('Colt', 'Steele', 'https://images.unsplash.com/photo-1628563694622-5a76957fd09c?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
  ('Rodolph', 'Van Romondt', 'https://lh3.googleusercontent.com/a/ACg8ocKCaB0i3DZctm3GL57I9ywQnnNe4nL_ix9mM8WBdubKIvE=s324-c-no'),
  ('David', 'Adewole', 'https://cdn.vectorstock.com/i/1000x1000/15/40/blank-profile-picture-image-holder-with-a-crown-vector-42411540.webp');

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title TEXT UNIQUE NOT NULL,
  content TEXT NOT NULL,
  user_id INTEGER REFERENCES users (id)
);

INSERT INTO posts (title, content, user_id)
VALUES
  ('First Post!', 'YALA', 2),
  ('Second Post!', 'YALA', 2),
  ('Third Post!', 'YALA', 2);