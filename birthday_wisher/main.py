import pandas  # Importing the pandas library for data manipulation
import datetime as dt  # Importing the datetime module as dt
import random  # Importing the random module for generating random numbers
import smtplib  # Importing the smtplib module for sending emails

MY_EMAIL = "mail"  # Sender's email address
MY_PASSWORD = "password"  # Sender's email password

today = dt.datetime.now()  # Getting the current date and time
today_tuple = (today.month, today.day)  # Creating a tuple with the current month and day

# Reading the birthday data from the CSV file into a DataFrame
data = pandas.read_csv('birthdays.csv')

# Creating a dictionary with birthday dates as keys and corresponding information as values
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Checking if today's date matches any birthday in the dictionary
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]  # Getting the information of the birthday person
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"  # Generating a random letter template file path

    # Opening and reading the contents of the selected letter template file
    with open(file_path) as text:
        content = text.read()
        updated_content = content.replace("[NAME]", birthday_person["name"])  # Replacing placeholder with the name

    # Sending a birthday email using SMTP with Gmail server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Initiating TLS encryption
        connection.login(MY_EMAIL, MY_PASSWORD)  # Logging in to the sender's email account
        connection.sendmail(from_addr=MY_EMAIL,  # Sending the email
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{updated_content}")
