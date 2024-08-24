USE movie_ticket_booking_system;
-- Create the Show table
CREATE TABLE Showtime (
    ShowTimeID INT NOT NULL AUTO_INCREMENT,
    MovieID INT NOT NULL,
    CinemaHallID INT NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (ShowTimeID),
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID),
    FOREIGN KEY (CinemaHallID) REFERENCES CinemaHall(CinemaHallID)
);

INSERT INTO Showtime (MovieID, CinemaHallID, Date, Time, Price)
VALUES
    (31, 1, '2023-08-05', '19:00:00', 15.00),
    (32, 2, '2023-08-05', '19:30:00', 16.00),
    (33, 3, '2023-08-05', '20:00:00', 17.00),
    (34, 4, '2023-08-05', '20:30:00', 18.00),
    (35, 5, '2023-08-06', '19:00:00', 19.00),
    (36, 6, '2023-08-06', '19:30:00', 20.00),
    (37, 7, '2023-08-06', '20:00:00', 21.00),
    (38, 8, '2023-08-06', '20:30:00', 22.00),
    (39, 9, '2023-08-07', '19:00:00', 23.00),
    (40, 10, '2023-08-07', '19:30:00', 24.00);
    
select * from showtime;


