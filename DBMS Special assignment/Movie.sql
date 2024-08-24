USE movie_ticket_booking_system;
-- Create the Movie table
CREATE TABLE Movie (
    MovieID INT NOT NULL AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL UNIQUE,
    Genre VARCHAR(255) NOT NULL,
    Language VARCHAR(255) NOT NULL,
    ReleaseDate DATE NOT NULL,
    Duration INT NOT NULL,
    PRIMARY KEY (MovieID)
);


INSERT INTO Movie (Title, Genre, Language, ReleaseDate, Duration)
VALUES
    ('Top Gun: Maverick', 'Action', 'English', '2022-05-27', 126),
    ('Jurassic World Dominion', 'Adventure', 'English', '2022-06-10', 147),
    ('Minions: The Rise of Gru', 'Animation', 'English', '2022-07-01', 87),
    ('Thor: Love and Thunder', 'Action', 'English', '2022-07-08', 119),
    ('The Batman', 'Action', 'English', '2022-03-04', 176),
    ('Everything Everywhere All at Once', 'Action', 'English', '2022-03-25', 139),
    ('Turning Red', 'Animation', 'English', '2022-03-11', 105),
    ('The Lost City', 'Action', 'English', '2022-03-25', 112),
    ('Cyrano', 'Drama', 'English', '2022-02-25', 123),
    ('Death on the Nile', 'Mystery', 'English', '2022-02-11', 127);


      select * from Movie;
  
