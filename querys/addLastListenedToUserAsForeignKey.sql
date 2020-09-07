ALTER TABLE users
ADD FOREIGN KEY (lastListened) REFERENCES music(musicId);