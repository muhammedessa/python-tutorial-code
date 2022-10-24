
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to Deposit & Withdrawal Machine!")

      
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("Amount Deposited: ",amount)
      
      
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdraw: ",amount)
        else:
            print("Insufficient balance ")
          
    def display(self):
        print("Your Available Balance=",self.balance)


      
#creating an object of class
s = Bank_Account()

#calling functions with that class
s.deposit()
s.withdraw()
s.display()
