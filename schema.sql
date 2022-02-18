CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    role INTEGER,
    UNIQUE(username)
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
    game_id INTEGER REFERENCES games ON DELETE CASCADE,
    platform_id INTEGER REFERENCES platforms,
    PRIMARY KEY (game_id, platform_id)
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category TEXT
);

CREATE TABLE games_categories (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories ON DELETE CASCADE
);

CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    time REAL,
    date TIMESTAMP,
    user_id INTEGER REFERENCES users,
    game_id INTEGER REFERENCES games ON DELETE CASCADE,
    platform_id INTEGER REFERENCES platforms,
    category_id INTEGER REFERENCES categories ON DELETE CASCADE
);
