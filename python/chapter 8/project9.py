class account:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.accountno=accountno
    def credit(self,amount):
            self.balance+=amount
            print("hi",amount,"you are credited")  
            print("total balance:-", self.get_balance())
    def debit(self,amount):
            self.balance-=amount
            print("hi",amount,"you are debited")  
            print("total balance:-", self.get_balance())
    def get_balance(self):
          return self.balance


s1=account(23000,1234567)         
s1.credit(1000)
s1.debit(200)

