###### Company example

```sql

CREATE TABLE Artist (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT
)

CREATE TABLE Genre (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT
)

CREATE TABLE Album (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
artist_id INTEGER,
title TEXT
)

CREATE TABLE Track (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT,
album_id INTEGER,
genre_id INTEGER,
len INTEGER, rating INTEGER, count INTEGER
)

INSERT INTO Artist (name) values ("Led Zepplin")
INSERT INTO Artist (name) values ("AC/DC")

INSERT INTO Genre (name) values ("Rock")
INSERT INTO Genre (name) values ("Metal")

INSERT INTO Album (title,artist_id) VALUES ("Who Made Who", 2);
INSERT INTO Album (title,artist_id) VALUES ("IV", 1)

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
VALUES ("Black Dog",5,297,0,2,1)

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
VALUES ("Stairway",5,482,0,2,1)

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
VALUES ("About to Rock",5,313,0,1,2)

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
VALUES ("Who Made Who",5,207,0,1,2)

```

###### Join
```sql
SELECT Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
SELECT Album.title, Artist.artist_id, Artist.id, Artist.name from Album join Artist on Album.artist_id = Artist.id
SELECT Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id
SELECT Track.title, Genre.name from Track join Genre
SELECT Track.title, Track.genre_id, Genre.id, Genre.name from Track join Genre
SELECT Track.title, Artist.name, Album.title, Genre.name from Track join Genre join Album join Artist on Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id

```
