# SanjaY
Simple Ticket booking system using Python

Created a simple ticket booking system using libraries like mysql.connector, smptlib, emailmessage, maskpass and time under python. 

I have used mysql as the base for basebase to store the data received from the user using mysqlconnector library.
After collection of the data a mail is sent to the user that they have fill the required details using smptlib library.
I have used email message to send the subject and body of the email.
I have used maskpass library instead of gatepass to hide the password provided by the user by showing them as *.
Maskpass does not work on your IDE. to make them work -> Click on the run tab - edit configurations - under configuration select Emulate terminal in output console. 
I have used the time library to slow down the print statement from appearing.


first I have written the code to create a database and tables for the data storing.
next i have asked the user to provide the information which will be stored to the database which will be used later on.
I gave option to the user for registering, booking and cancelling of the booked tickets.
I have used global keyboard to used the information gathered in the function to be used else where.

In the booking option you cannot use it without registering as it checks with the database to see whether you are registerred user or not.
In the cancellation option you cannot use it without booking a ticket.

after registering, booking and cancelling of a ticket the user is intimated through a mail. 
