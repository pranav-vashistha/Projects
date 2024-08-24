USE movie_ticket_booking_system;
-- Create the Ticket table
CREATE TABLE Ticket (
    TicketID INT NOT NULL AUTO_INCREMENT,
    ShowID INT NOT NULL,
    CustomerID INT NOT NULL,
    SeatNumber INT NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (TicketID),
    FOREIGN KEY (ShowID) REFERENCES showtime(ShowTimeID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);


INSERT INTO Ticket (ShowID, CustomerID, SeatNumber, Price)
VALUES
    (21, 1, 1, 15.00),
    (22, 2, 2, 16.00),
    (23, 3, 3, 17.00),
    (24, 4, 4, 18.00),
    (25, 5, 5, 19.00),
    (26, 6, 6, 20.00),
    (27, 7, 7, 21.00),
    (28, 8, 8, 22.00),
    (29, 9, 9, 23.00),
    (30, 10, 10, 24.00);
    
select * from Ticket;
