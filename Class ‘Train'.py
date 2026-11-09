# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint

class train:
    
    def __init__(self,trainNO):
        self.trainNO=trainNO
        
    def bookticket(self,fro,to):
        print(f"THE TRAIN NUMBER:{self.trainNO} IS MOVIG FROM {fro} to {to}")
    def getstatus(self):
        print(f"THE TRAIN NUMBER {self.trainNO} on the way to the destinations")
    def fareinformation(self):
        print(f"THE TRAIN NUMBER {self.trainNO} IS BOOKED WITH THE FARE OF ONE SLEEPER IS {randint(100,2567)}")
        
s1=train(1101221025)
s1.bookticket("chennai","goa")
s1.getstatus()
s1.fareinformation()
