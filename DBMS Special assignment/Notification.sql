USE movie_ticket_booking_system;
-- Create the Notification table
CREATE TABLE Notification (
    NotificationID INT NOT NULL AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    Message VARCHAR(255) NOT NULL,
    Date DATE NOT NULL,
    PRIMARY KEY (NotificationID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

INSERT INTO Notification (CustomerID, Message, Date)
VALUES
    (1, 'Your booking for ShowTimeID 1 has been confirmed.', '2023-08-05'),
    (2, 'Your booking for ShowTimeID 2 has been confirmed.', '2023-08-05'),
    (3, 'Your booking for ShowTimeID 3 has been confirmed.', '2023-08-05'),
    (4, 'Your booking for ShowTimeID 4 has been confirmed.', '2023-08-05'),
    (5, 'Your booking for ShowTimeID 5 has been confirmed.', '2023-08-06'),
    (6, 'Your booking for ShowTimeID 6 has been confirmed.', '2023-08-06'),
    (7, 'Your booking for ShowTimeID 7 has been confirmed.', '2023-08-06'),
    (8, 'Your booking for ShowTimeID 8 has been confirmed.', '2023-08-06'),
    (9, 'Your booking for ShowTimeID 9 has been confirmed.', '2023-08-07'),
    (10, 'Your booking for ShowTimeID 10 has been confirmed.', '2023-08-07');

    select * from Notification;
