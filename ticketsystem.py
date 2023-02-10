import time
import mysql.connector
import maskpass
import smtplib
from email.message import EmailMessage

mydb = mysql.connector.connect( host="localhost",user="root",password="root", database="ticket_reservation_system")
mycursor = mydb.cursor()
mycursor.execute("Create database if not exists ticket_reservation_system")
try:
    mycursor.execute("CREATE TABLE if not exists User_table (sno int primary key not null auto_increment, name varchar(60)"
                     ",username Varchar(60), phone_no int(20), email varchar(100), password varchar(100))")
    mycursor.execute("CREATE TABLE if not exists Destination_table (sno int primary key not null auto_increment, destination varchar(60)"
                     ", seats_availability int)")
except:
    pass


def mail():
    em = EmailMessage()
    em['From'] = "EMAILID"
    em['To'] = email
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login("EMAILID", "password")
        server.sendmail('"EMAILID"', email, em.as_string())
        print("Mail sent successfully")
        server.quit()

def register():
    global body
    global email
    global subject
    name = input("Please enter your name: \n")
    username = input("Please provide your username: \n")
    phone = int(input("Please enter your phone number: \n"))
    email = input("Please enter you email Id: \n")
    password = maskpass.askpass("Please enter password: \n")
    while True:
        confirm = maskpass.askpass("Please re-enter password: \n")
        if password == confirm:
            conpass = password
            break
    sqlinsert = "insert into User_table(name,username,phone_no,email,password) values(%s,%s,%s,%s,%s)"
    fromnoro = [(name, username, phone, email, conpass)]
    mycursor.executemany(sqlinsert, fromnoro)
    mydb.commit()
    body = name," your details registered Successfully"
    subject = "ticket reservation system"
    mail()


def login():
    print("""
please login to continue 
    """)
    time.sleep(3)
    global email
    global passwo
    while True:
        while True:
            email = input("Email ID: ")
            passwo = maskpass.askpass("Password: ")
            check = "SELECT email FROM User_table where email = %s"
            val = (passwo, email)
            mycursor.execute(check, (email,))
            myresult = mycursor.fetchall()
            if myresult:
                break
            else:
                spell = input("Do you want to register (Y/N): ").lower()
                if spell == "y":
                    register()
                    break
        cross_check = "SELECT username FROM User_table WHERE password = %s AND email = %s"
        mycursor.execute(cross_check, val)
        myresult = mycursor.fetchall()
        if myresult:
            print("Login successful")
            break
        else:
            print("Login failed")
            print("Try again")

def booking():
    global body
    global subject
    global ticket
    global how
    print("Welcome to the booking portal")
    print("""
Choose a destination you want to travel to:

1) Chennai to Pune
2) Chennai to Delhi
3) Chennai to Hyderabad
4) Chennai to KolKata 
        """)
    inp = int(input("Where do you want to travel (1 to 4): "))

    if inp == 1:
        mycursor.execute("SELECT destination, seats_availability from Destination_table where sno = 1")
        myresult = mycursor.fetchall()
        for y in myresult:
            print(y)
        print("")
        while True:
            how = int(input("How many tickets do you need:  "))
            if how > y[1] or how < 0:
                print("It must be with in the available tickets")
            else:
                break
        if how > 0:
            ticket = ("Chennai to Pune", how)
            mycursor.execute("SELECT seats_availability from Destination_table WHERE sno = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                pass
            x= x[0]
            result = (x - how)
            up = "UPDATE Destination_table SET seats_availability = %s WHERE sno = 1"
            mycursor.execute(up, (result,))
            mydb.commit()
            time.sleep(2)
            print("Ticket Booked Successfully")
            data = ("SELECT name from user_table WHERE email = %s")
            mycursor.execute(data, (email,))
            myresult = mycursor.fetchall()
            for z in myresult:
                pass
            send = z[0], " - ", y[0], str(how), "Ticket Booked Successfully"
            empty = []
            for i in send:
                empty.append(i)
            d = empty[0] + " " + empty[1] + " " + empty[2] + " " + empty[3] + " " + empty[4]
            print(d)
            body = d
            subject = "Ticket reservation system Booking Status"
            mail()

    elif inp == 2:
        mycursor.execute("SELECT destination, seats_availability from Destination_table where sno = 2")
        myresult = mycursor.fetchall()
        for y in myresult:
            print(y)
        print("")
        while True:
            how = int(input("How many tickets do you need:  "))
            if how > y[1] or how < 0:
                print("It must be with in the available tickets")
            else:
                break
        if how > 0:
            ticket = ("Chennai to Pune", how)
            mycursor.execute("SELECT seats_availability from Destination_table WHERE sno = 2")
            myresult = mycursor.fetchall()
            for x in myresult:
                pass
            x = x[0]
            result = (x - how)
            up = "UPDATE Destination_table SET seats_availability = %s WHERE sno = 2"
            mycursor.execute(up, (result,))
            mydb.commit()
            time.sleep(2)
            print("Ticket Booked Successfully")
            data = ("SELECT name from user_table WHERE email = %s")
            mycursor.execute(data, (email,))
            myresult = mycursor.fetchall()
            for z in myresult:
                pass
            send = z[0], " - ", y[0], str(how), "Ticket Booked Successfully"
            empty = []
            for i in send:
                empty.append(i)
            d = empty[0] + " " + empty[1] + " " + empty[2] + " " + empty[3] + " " + empty[4]
            print(d)
            body = d
            subject = "Ticket reservation system Booking Status"
            mail()

    elif inp == 3:
        mycursor.execute("SELECT destination, seats_availability from Destination_table where sno = 3")
        myresult = mycursor.fetchall()
        for y in myresult:
            print(y)
        print("")
        while True:
            how = int(input("How many tickets do you need:  "))
            if how > y[1] or how < 0:
                print("It must be with in the available tickets")
            else:
                break
        if how > 0:
            ticket = ("Chennai to Pune", how)
            mycursor.execute("SELECT seats_availability from Destination_table WHERE sno = 3")
            myresult = mycursor.fetchall()
            for x in myresult:
                pass
            x = x[0]
            result = (x - how)
            up = "UPDATE Destination_table SET seats_availability = %s WHERE sno = 3"
            mycursor.execute(up, (result,))
            mydb.commit()
            time.sleep(2)
            print("Ticket Booked Successfully")
            data = ("SELECT name from user_table WHERE email = %s")
            mycursor.execute(data, (email,))
            myresult = mycursor.fetchall()
            for z in myresult:
                pass
            send = z[0], " - ", y[0], str(how), "Ticket Booked Successfully"
            empty = []
            for i in send:
                empty.append(i)
            d = empty[0] + " " + empty[1] + " " + empty[2] + " " + empty[3] + " " + empty[4]
            print(d)
            body = d
            subject = "Ticket reservation system Booking Status"
            mail()

    elif inp == 4:
        mycursor.execute("SELECT destination, seats_availability from Destination_table where sno = 4")
        myresult = mycursor.fetchall()
        for y in myresult:
            print(y)
        print("")
        while True:
            how = int(input("How many tickets do you need:  "))
            if how > y[1] or how < 0:
                print("It must be with in the available tickets")
            else:
                break
        if how > 0:
            ticket = ("Chennai to Pune", how)
            mycursor.execute("SELECT seats_availability from Destination_table WHERE sno = 4")
            myresult = mycursor.fetchall()
            for x in myresult:
                pass
            x = x[0]
            result = (x - how)
            up = "UPDATE Destination_table SET seats_availability = %s WHERE sno = 4"
            mycursor.execute(up, (result,))
            mydb.commit()
            time.sleep(2)
            print("Ticket Booked Successfully")
            data = ("SELECT name from user_table WHERE email = %s")
            mycursor.execute(data, (email,))
            myresult = mycursor.fetchall()
            for z in myresult:
                pass
            send = z[0], " - ", y[0], str(how), "Ticket Booked Successfully"
            empty = []
            for i in send:
                empty.append(i)
            d = empty[0] + " " + empty[1] + " " + empty[2] + " " + empty[3] + " " + empty[4]
            print(d)
            body = d
            subject = "Ticket reservation system Booking Status"
            mail()

# it is used for creating the table
# destinsert = "insert into Destination_table(destination,seats_availability) values(%s,%s)"
# fordest = [("Chennai to Pune", 10),("Chennai to Delhi", 10),("Chennai to Hyderabad", 10),("Chennai to Kolkata",10)]
# mycursor.executemany(destinsert,fordest)
# mydb.commit()


def cancel():
    global body
    global subject
    login()
    do = input("Do you want to cancel the your ticket(y/n): ").lower()
    if do == "y":
        try:
            print(ticket)
            while True:
                how = int(input("How many tickets do you want to cancel: "))
                if ticket[1] == how or ticket[1] > how:
                    if ticket[0] == "Chennai to Pune":
                        mycursor.execute("SELECT seats_availability from Destination_table WHERE sno = 1")
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            pass
                        x = x[0]
                        result = (x + how)
                        up = "UPDATE Destination_table SET seats_availability = %s WHERE sno = 1"
                        mycursor.execute(up, (result,))
                        mydb.commit()
                        time.sleep(3)
                        print("Ticket cancelled Successfully")
                        body = "Ticket cancelled Successfully"
                        subject = "Ticket reservation system Booking Status"
                        mail()
                        break
                    elif ticket[0] == "Chennai to Delhi":
                        mycursor.execute("SELECT seats_availability from Destination_table WHERE sno = 2")
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            pass
                        x = x[0]
                        result = (x + how)
                        up = "UPDATE Destination_table SET seats_availability = %s WHERE sno = 2"
                        mycursor.execute(up, (result,))
                        mydb.commit()
                        time.sleep(3)
                        print("Ticket cancelled Successfully")
                        body = "Ticket cancelled Successfully"
                        subject = "Ticket reservation system Booking Status"
                        mail()
                        break
                    elif ticket[0] == "Chennai to Hyderabad":
                        mycursor.execute("SELECT seats_availability from Destination_table WHERE sno = 3")
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            pass
                        x = x[0]
                        result = (x + how)
                        up = "UPDATE Destination_table SET seats_availability = %s WHERE sno = 3"
                        mycursor.execute(up, (result,))
                        mydb.commit()
                        time.sleep(3)
                        print("Ticket cancelled Successfully")
                        body = "Ticket cancelled Successfully"
                        subject = "Ticket reservation system Booking Status"
                        mail()
                        break
                    elif ticket[0] == "Chennai to Kolkata":
                        mycursor.execute("SELECT seats_availability from Destination_table WHERE sno = 4")
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            pass
                        x = x[0]
                        result = (x + how)
                        up = "UPDATE Destination_table SET seats_availability = %s WHERE sno = 4"
                        mycursor.execute(up, (result,))
                        mydb.commit()
                        time.sleep(3)
                        print("Ticket cancelled Successfully")
                        body = "Ticket cancelled Successfully"
                        subject = "Ticket reservation system Booking Status"
                        mail()
                        break
        except:
            print("You have not booked any tickets")

print("Welcome to ticket reservation system")
time.sleep(3)
while True:
    print('''
 1) Register
 2) Ticket booking
 3) Cancel ticket
 4) Exit
    ''')
    user = input("Please mention option (1 to 5): \n")

    if user == "1":
        register()
        previous = input("Previous screen(y/n): ").lower()
        if previous == "y":
            print("Reservation System")
            time.sleep(2)

        elif previous != "y":
            print("good bye")
            break

    elif user == "2":
        login()
        booking()
        while True:
            previous = input("Previous booking screen (1), main menu (2): ").lower()
            if previous == "1":
                booking()
            elif previous == "2":
                break

    elif user == "3":
        cancel()
        previous = input("Previous screen(y/n): ").lower()
        if previous == "y":
            print("Reservation System")
            time.sleep(2)

        elif previous != "y":
            print("good bye")
            break

    elif user == "4":
        print("Thank you")
        break
