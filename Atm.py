class Atm(object):
    def __init__(self, pinNumber, cardNumber):
       self.pinNumber = pinNumber
       self.cardNumber = cardNumber
    
    def cashWithDrawal(self):
        print("Rs.2000 has been withdrawed")

    def balanceEnquiry(self):
        print("Your current balance is : Rs.5000")

    def cashTransfer(self):
        print("Rs.1000 has been trensfered")
    
    def cashDeposit(self):
        deposit = input("How much would you like to deposit : ")
        print("Rs.",deposit," has been deposited")
    

    

userCard = input("Enter your card number : ")
userPin = input("Enter your pin number : ")
user = Atm(userPin,userCard);

print("A - Cash withdrawal , B - Balance Enquiry , C - Cash Transfer , D - Cash Deposit")

action=input("What would you like to do ?? (Type the letter acording to the above given info ) : ")

if (action == 'A'):
    print(user.cashWithDrawal())

if (action == 'B'):
    print(user.balanceEnquiry())

if (action == 'C'):
    print(user.cashTransfer())

if (action == 'D'):
    print(user.cashDeposit())

