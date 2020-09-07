ALTER TABLE music
ADD FOREIGN KEY (artist) REFERENCES artist(username);