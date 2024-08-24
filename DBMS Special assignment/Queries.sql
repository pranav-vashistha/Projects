SELECT NotificationID, Message, Date
FROM Notification
WHERE CustomerID = 1;

SELECT BookingID, ShowtimeID, TicketID, PaymentID, Date
FROM Booking
WHERE CustomerID = 1;


SELECT Title, ReleaseDate
FROM Movie
UNION
SELECT Name, Location
FROM CinemaHall;

SELECT Showtime.MovieID, Showtime.CinemaHallID, Showtime.Date, Showtime.Time, Customer.Name, Ticket.SeatNumber
FROM Ticket
JOIN Showtime ON Ticket.ShowID = Showtime.ShowTimeID
JOIN Customer ON Ticket.CustomerID = Customer.CustomerID
JOIN Payment ON Ticket.TicketID = Payment.TicketID
WHERE Payment.PaymentType = 'Credit Card';

SELECT Name, Email
FROM Customer;

SELECT Name, Location
FROM CinemaHall;

SELECT Showtime.MovieID, Showtime.CinemaHallID, Showtime.Date, Showtime.Time
FROM Showtime
JOIN Movie ON Showtime.MovieID = Movie.MovieID
WHERE Movie.Genre = 'action'
AND DAYOFWEEK(Showtime.Date) IN ('Friday', 'Saturday');

