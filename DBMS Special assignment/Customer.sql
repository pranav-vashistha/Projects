CREATE DATABASE movie_ticket_booking_system;

USE movie_ticket_booking_system;
-- Create the Customer table
CREATE TABLE Customer (
    CustomerID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    PRIMARY KEY (CustomerID)
);


INSERT INTO Customer (Name, Email, PhoneNumber, Address, DateOfBirth)
VALUES
    ('John Doe', 'john.doe@example.com', '+15555555555', '123 Main Street, Anytown, CA 91234', '1980-01-01'),
    ('Jane Doe', 'jane.doe@example.com', '+15555555556', '456 Elm Street, Anytown, CA 91234', '1982-02-02'),
    ('Peter Parker', 'peter.parker@example.com', '+15555555557', '789 Oak Street, Anytown, CA 91234', '1984-03-03'),
    ('Mary Jane Watson', 'maryjane.watson@example.com', '+15555555558', '1011 Maple Street, Anytown, CA 91234', '1986-04-04'),
    ('Harry Osborn', 'harry.osborn@example.com', '+15555555559', '1213 Pine Street, Anytown, CA 91234', '1988-05-05'),
    ('Gwen Stacy', 'gwen.stacy@example.com', '+15555555560', '1415 Elm Street, Anytown, CA 91234', '1990-06-06'),
    ('Flash Thompson', 'flash.thompson@example.com', '+15555555561', '1617 Oak Street, Anytown, CA 91234', '1992-07-07'),
    ('Betty Brant', 'betty.brant@example.com', '+15555555562', '1819 Maple Street, Anytown, CA 91234', '1994-08-08'),
    ('J. Jonah Jameson', 'j.jonah.jameson@example.com', '+15555555563', '2021 Pine Street, Anytown, CA 91234', '1996-09-09'),
    ('Robbie Robertson', 'robbie.robertson@example.com', '+15555555564', '2223 Elm Street, Anytown, CA 91234', '1998-10-10');

SELECT * FROM Customer;