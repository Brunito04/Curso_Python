import smtplib

# Your email goes here
my_email = "brunitotest@gmail.com"
password = "Huqz3snrybwVL3"

# Smtp direction goes here
with smtplib.SMTP("smtp.gmail.com") as connection:

    # Encrypts the email if intercepted
    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="bruno2004b@gmail.com",
        msg="Subject:Title\n\nBody of the email"
    )

