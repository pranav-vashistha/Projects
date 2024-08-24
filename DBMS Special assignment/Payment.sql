USE movie_ticket_booking_system;
-- Create the Payment table
CREATE TABLE Payment (
    PaymentID INT NOT NULL AUTO_INCREMENT,
    TicketID INT NOT NULL,
    PaymentType VARCHAR(255) NOT NULL,
    Amount DECIMAL(10,2) NOT NULL,
    Date DATE NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (TicketID) REFERENCES Ticket(TicketID)
);

INSERT INTO Payment (TicketID, PaymentType, Amount, Date)
VALUES
    (11, 'Credit Card', 15.00, '2023-08-05'),
    (12, 'Debit Card', 16.00, '2023-08-05'),
    (13, 'Net Banking', 17.00, '2023-08-05'),
    (14, 'UPI', 18.00, '2023-08-05'),
    (15, 'Wallet', 19.00, '2023-08-06'),
    (16, 'Cash on Delivery', 20.00, '2023-08-06'),
    (17, 'Credit Card', 21.00, '2023-08-06'),
    (18, 'Debit Card', 22.00, '2023-08-06'),
    (19, 'Net Banking', 23.00, '2023-08-07'),
    (20, 'UPI', 24.00, '2023-08-07');


select * from payment;