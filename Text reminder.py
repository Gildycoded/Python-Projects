#! python3
import os, time, subprocess, datetime, schedule
from dotenv import load_dotenv
from twilio.rest import Client

#Phone numbers
twilioNUMBER= os.getenv('TWILIO_NUMBER')
myNUM = os.getenv('MY_NUMBER')

#Send Text INFO
SID= os.getenv('TWILIO_ACCOUNT_SID')
authTOKEN= os.getenv('TWILIO_AUTH_TOKEN')
client = Client(SID, authTOKEN)

#Write the Message
def message():
    client.messages.create(
                        body='Did you bend your knee today?',
                        from_= twilioNUMBER,
                        to = '+XXXXXXXXXX'

                    )
#Have it do it every blank time
schedule.every(10).seconds.do(message)

while True:
    schedule.run_pending()
    time.sleep(1)

