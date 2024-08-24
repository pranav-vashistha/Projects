USE movie_ticket_booking_system;
-- Create the Seat table
CREATE TABLE Seat (
    SeatID INT NOT NULL AUTO_INCREMENT,
    ScreenID INT NOT NULL,
    RowNumber INT NOT NULL,
    ColumnNumber INT NOT NULL,
    PRIMARY KEY (SeatID),
    FOREIGN KEY (ScreenID) REFERENCES Screen(ScreenID)
);

INSERT INTO Seat (ScreenID, RowNumber, ColumnNumber)
VALUES
    (1, 1, 1),
    (1, 1, 2),
    (1, 2, 1),
    (1, 2, 2),
    (2, 1, 1),
    (2, 1, 2),
    (2, 2, 1),
    (2, 2, 2),
    (3, 1, 1),
    (3, 1, 2),
    (3, 2, 1),
    (3, 2, 2);

    select * from Seat;
