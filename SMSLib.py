from twilio.rest import Client
from Konfig import *



class SMSActions:

    def __init__(self):
        # Your Account SID from twilio.com/console
        self.account_sid = ACCOUNT_SID
        # Your Auth Token from twilio.com/console
        self.auth_token  = AUTH_TOKEN
        #Create instance of client
        self.client = Client(self.account_sid, self.auth_token)
        self.ToNumber=TO
        self.FromNumber=FROM_

    def SendSMS(self,Message,ToNumber,FromNumber):
        message = self.client.messages.create(
            # To Whom send the message
            to=ToNumber,
            # Your Account Phone Number
            from_=FromNumber,

        body="Hello from Python!")

        print(message.sid)


    def ReceivedSMS(self):

        pass

        return Message