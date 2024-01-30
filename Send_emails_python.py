import smtplib

my_email = 'sunriserscap@gmail.com'
password = "odkybhvwgrycymjk"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()#it for encrypting your message by transfer layer security
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs="hiteshpydeveloper@gmail.com",
                    msg="Subject:Hello Rahul \n\n This is the body of my email ")
connection.close()