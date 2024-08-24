CREATE TABLE Booking (
    BookingID INT NOT NULL AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ShowTimeID INT NOT NULL,
    TicketID INT NOT NULL,
    PaymentID INT NOT NULL,
    Date DATE NOT NULL,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ShowTimeID) REFERENCES ShowTime(ShowTimeID) ON DELETE CASCADE,
    FOREIGN KEY (TicketID) REFERENCES Ticket(TicketID) ON DELETE CASCADE,
    FOREIGN KEY (PaymentID) REFERENCES Payment(PaymentID) ON DELETE CASCADE
);


INSERT INTO Booking (CustomerID, ShowTimeID, TicketID, PaymentID, Date)
VALUES
    (1,21, 11, 1, '2023-08-05'),
    (2, 22, 12, 2, '2023-08-05'),
    (3, 23, 13, 3, '2023-08-05'),
    (4, 24, 14, 4, '2023-08-05'),
    (5, 25, 15, 5, '2023-08-06'),
    (6, 26, 16, 6, '2023-08-06'),
    (7, 27, 17, 7, '2023-08-06'),
    (8, 28, 18, 8, '2023-08-06'),
    (9, 29, 19, 9, '2023-08-07'),
    (10, 30, 20, 10, '2023-08-07');
    
    select * from Booking;


