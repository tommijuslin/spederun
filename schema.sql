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
    game_id INTEGER REFERENCES games,
    platform_id INTEGER REFERENCES platforms,
    PRIMARY KEY (game_id, platform_id)
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category TEXT
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

INSERT INTO platforms (name)
VALUES
    ('PC'),
    ('PlayStation 1'),
    ('PlayStation 2'),
    ('PlayStation 3'),
    ('PlayStation 4'),
    ('PlayStation 5'),
    ('PlayStation Portable'),
    ('PlayStation Vita'),
    ('NES'),
    ('Super Nintendo'),
    ('Nintendo 64'),
    ('Nintendo Gamecube'),
    ('Nintendo Wii'),
    ('Nintendo Wii U'),
    ('Nintendo Switch'),
    ('Nintendo Game Boy'),
    ('Nintendo Game Boy Advance'),
    ('Nintendo DS'),
    ('Nintendo 3DS'),
    ('Xbox'),
    ('Xbox 360'),
    ('Xbox One'),
    ('Xbox Series X');
