import smtplib
import random
import datetime as dt

# Here put the email address, password, receiver email
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "PASSWORD"
RECEIVER_EMAIL = "RECEIVER EMAIL"

quotes_dict = {}

now = dt.datetime.now()
weekday = now.weekday()

# Send motivated quote on every Monday
if weekday == 1:
    try:
        # Odczytaj plik tekstowy
        with open("quotes.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Not found a file")
    else:
        # Utwórz słownik
        for i, line in enumerate(lines, start=0):
            if "-" in line:
                quote, author = line.split(" - ", 1)
                author = author.strip()
                quote = quote.strip()
                quotes_dict[i] = {"quote": quote, "author": author}
    random_quote = random.choice(quotes_dict)

    # For Gmail: smtp.gmail.com | Hotmail: smtp.live.com | Yahoo: smtp.mail.yahoo.com
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Motivational Quote\n\n{random_quote["quote"]}\n \n{random_quote["author"]}")
