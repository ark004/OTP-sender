import random
from twilio.rest import Client

otp = random.randint(1000,9999)

account_sid = "Aawsexdrcftgvbhjnkml,kmjhbvgcvhbvgh"
auth_token = "wsedrftgyhujikl,,kjhugyftdrrfghgvhb"

client = Client(account_sid, auth_token)
msg = client.messages.create(
    body = f"your otp is {otp}",
    from_ = "+144448554544",
    to = "+18 9955662247"
)