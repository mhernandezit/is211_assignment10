/*
Michael Hernandez
IS211
Music Database
*/

CREATE TABLE artist 
  ( 
     artist_id   INTEGER PRIMARY KEY, 
     artist_name TEXT NOT NULL 
  ); 

CREATE TABLE album 
  ( 
     album_id   INTEGER PRIMARY KEY, 
     album_name TEXT NOT NULL, 
     artist_id  INTEGER NOT NULL, 
     FOREIGN KEY (artist_id) REFERENCES artist(artist_id) 
  ); 

CREATE TABLE songs 
  ( 
     song_id      INTEGER PRIMARY KEY, 
     song_name    TEXT NOT NULL, 
     artist_id    INTEGER NOT NULL, 
     album_id     INTEGER, 
     track_number INTEGER, 
     song_length  INTEGER, 
     FOREIGN KEY (artist_id) REFERENCES artist(artist_id), 
     FOREIGN KEY (album_id) REFERENCES album(album_id) 
  ); 
