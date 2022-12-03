class ATM:
    def __init__(self,name,cardnumber,cardpin,balance):
        self.name=name
        self.cardnumber=cardnumber
        self.cardpin=cardpin
        self.balance=balance
    def checkbalance(self):
        p = int(input('what is your cardpin '))
        if p==self.cardpin:
            print("your current balance is"+str(self.balance))
        else:
            print('invalid cardpin')
    def depositmoney(self):
        p = int(input('what is your cardpin '))
        if p==self.cardpin:
            a=int(input("how much do you want to deposit"))
            self.balance=self.balance+a
            print('your new balance is '+str(self.balance))
        else:
            print('your card number is invalid')
    def withdrawmoney(self):
        p = int(input('what is your cardpin '))
        if p==self.cardpin:
            a=int(input('how much do you want to withdraw'))
            if a<=self.balance:
                self.balance=self.balance-a
                print('your current balance is '+str( self.balance ))
            else:
                print('insufficiant funds')
        else:
            print('invalid cardpin')
        
customer1 = ATM("vihaan",1234567890,1234,120000)
customer1.withdrawmoney()
 