class BankAccount:
    def __init__(self,full_name,account_number,routing_number,balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

def deposit(self,amount):
    self.balance += amount

def withdraw(self,amount):
    overdraft= 10
    if self.balance>=amount:
        self.balance-=amount
        print("You withdrew:$",amount)
    else:
        self.balance + overdraft = amount
        print("Your balance is insufficient")
    
def getbalance():
    return balance
    print(f"Hello {full_name}! Your balance is {balance}")


        