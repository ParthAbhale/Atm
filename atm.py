class Atm(object):
    def __init__(self,name,cardNo,pinNo,banckname,cashToWid):
        self.name = name
        self.cardNo = cardNo
        self.pinNo = pinNo
        self.banckname = banckname
        self.cashToWid = cashToWid
    def welcome(self):
        print(f"Hello {self.name},Welcome to {self.banckname} bank")
    def cashWidrawal(self):
        print(f"Cash WIDRAWED SUCCESSFULLY,The Amount was {self.cashToWid}")

card = Atm("Parth",98,95,"Union",500)
card.welcome()
print(f"Your Card Number: {card.cardNo}")
print(f"Your Pin Number: {card.pinNo}")
card.cashWidrawal()
