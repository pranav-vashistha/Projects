USE movie_ticket_booking_system;
-- Create the Screen table
CREATE TABLE Screen (
    ScreenID INT NOT NULL AUTO_INCREMENT,
    CinemaHallID INT NOT NULL,
    NumberOfSeats INT NOT NULL,
    PRIMARY KEY (ScreenID),
    FOREIGN KEY (CinemaHallID) REFERENCES CinemaHall(CinemaHallID)
);

INSERT INTO Screen (CinemaHallID, NumberOfSeats)
VALUES
    (1, 50),
    (2, 70),
    (3, 30),
    (4, 40),
    (5, 60),
    (6, 80),
    (7, 20),
    (8, 100),
    (9, 90),
    (10, 10);
    
    
    select * from Screen;
