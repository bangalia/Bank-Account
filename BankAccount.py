from random import random 

class BankAccount:
    routing_number = 162738490

class BankAccount:
    def __init__(self,full_name,account_number,balance):
        self.full_name = full_name
        self.account_number = randint()
        self.balance = int(balance)
        
def deposit(self,amount):
    self.balance += amount
    amount = input("How much would you like to deposit?")
print(f"Amount deposited was ${amount}")

def withdraw(self,amount):
    overdraft= 10
    amount = int(input("How much would you like to withdraw?"))
    if self.balance>=amount:
        self.balance-=amount
        print("You withdrew:$",amount)
    else:
        self.balance + overdraft = negbalance
        print("Your balance is insufficient")

    
def getbalance():
    return balance
    print(f"Hello {full_name}! Your balance is {balance}")

def addinterest():
    interest = balance * 0.00083
    newbalance = balance + interest 

def print_receipt():
    print(full_name)
    print(account_number)
    print(routing_number)
    print(balance)

amanda = BankAccount("Amanda_Fuller",account_number,2380)

amanda.getbalance()

phil = BankAccount("Phil Collins",account_number,763)

phil.print_receipt()

charles = BankAccount("Charles Bronson",account_number,25)