CREATE TABLE mainNoteAppUsers
(
id  SERIAL PRIMARY KEY,
username text  NOT NULL UNIQUE ,
pwd text NOT NULL,
HTML text NOT NULL
);