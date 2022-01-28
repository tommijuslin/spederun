CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    title TEXT
);

CREATE TABLE platforms (
    id SERIAL PRIMARY KEY,
    name TEXT,
    UNIQUE(name)
);

CREATE TABLE games_platforms (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games,
    platform_id INTEGER REFERENCES platforms
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE games_categories (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games,
    category_id INTEGER REFERENCES categories
);

CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    time REAL,
    date TIMESTAMP,
    user_id INTEGER REFERENCES users,
    game_id INTEGER REFERENCES games,
    platform_id INTEGER REFERENCES platforms,
    category_id INTEGER REFERENCES categories
);
