CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE topic (
    id SERIAL PRIMARY KEY,
    name TEXT,
    content TEXT,
    category_id INTEGER REFERENCES category,
    times TIMESTAMP DEFAULT NOW(),
    created_by INTEGER REFERENCES users
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    content TEXT,
    topic_id INTEGER REFERENCES topic,
    times TIMESTAMP DEFAULT NOW(),
    created_by INTEGER REFERENCES users
);

CREATE TABLE contact (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    message TEXT
);



