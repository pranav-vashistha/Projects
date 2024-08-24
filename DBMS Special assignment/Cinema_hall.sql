USE movie_ticket_booking_system;
-- Create the CinemaHall table
CREATE TABLE CinemaHall (
    CinemaHallID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL UNIQUE,
    Location VARCHAR(255) NOT NULL,
    NumberOfScreens INT NOT NULL,
    PRIMARY KEY (CinemaHallID)
);

INSERT INTO CinemaHall (Name, Location, NumberOfScreens)
VALUES
    ('Cinema 1', '123 Main Street, Anytown, CA 91234', 5),
    ('Cinema 2', '456 Elm Street, Anytown, CA 91234', 7),
    ('Cinema 3', '789 Oak Street, Anytown, CA 91234', 3),
    ('Cinema 4', '1011 Maple Street, Anytown, CA 91234', 4),
    ('Cinema 5', '1213 Pine Street, Anytown, CA 91234', 6),
    ('Cinema 6', '1415 Elm Street, Anytown, CA 91234', 8),
    ('Cinema 7', '1617 Oak Street, Anytown, CA 91234', 2),
    ('Cinema 8', '1819 Maple Street, Anytown, CA 91234', 10),
    ('Cinema 9', '2021 Pine Street, Anytown, CA 91234', 9),
    ('Cinema 10', '2223 Elm Street, Anytown, CA 91234', 1);
    
select * from CinemaHall;
