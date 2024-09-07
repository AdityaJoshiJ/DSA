import math
import random


class Bank():
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def createAccount(self, customer, firstDeposit=0):
        accountNumber = self.generateAccountNumber()
        account = BankAccount(customer, accountNumber)
        self.customers[accountNumber] = account
        customer.deposit(firstDeposit)
        print(
            f"Account created for {customer.name}. Account number: {accountNumber}")

    def get_account(self, accountNumber):
        return self.customers.get(accountNumber)

    def generateAccountNumber(self):
        def cardGen():
            n = random.random()
            ranCard = math.floor(n*pow(10, 12)+1)
            even = 0
            odd = 0
            temp = ranCard
            while temp > 0:
                odd += temp % 10
                temp = temp//10
                even += temp % 10
                temp = temp//10
            if (odd*2+even) % 10 == 0:
                return ranCard
            else:
                return cardGen()
        return cardGen()


class BankAccount():
    def __init__(self, customer, accountNumber):
        self.customer = customer
        self.accountNumber = accountNumber

    def deposit(self, amount):
        self.customer.deposit(amount)

    def withdraw(self, amount):
        self.customer.withdraw(amount)

    def transfer(self, anotherAccount, amount):
        self.customer.transfer(anotherAccount, amount)

    def show_details(self):
        self.customer.show_details()


class customer():
    def __init__(self, name, accountNumber, firstDeposit=0):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = firstDeposit
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposit - {amount:.2f}")
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def withdeaw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
            return
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdeow - {amount:.2f}")
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def transfer(self, anotherAccount, amount):
        if amount <= 0:
            print("Invalid transfer amount. Please enter a positive value.")
            return
        if amount > self.balance:
            print("Insufficient funds for transfer.")
            return
        self.balance -= amount
        anotherAccount.balance += amount
        self.transaction_history.append(
            f"Transfer - {amount:.2f} to {anotherAccount.accountNumber})")
        print(
            f"Transferred {amount:.2f} to {anotherAccount.name}. New balance: {self.balance:.2f}")

    def show_details(self):
        print("Customer Name:", self.name)
        print("Account Number:", self.accountNumber)
        print("Balance:", self.balance)
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)


bank = Bank("MyBank")
customer1 = customer("Aditya Joshi", "123456")
bank.createAccount(customer1, 1000000)

customer2 = customer("Vishw Faldu", "234567")
bank.createAccount(customer2, 50000)

customer1.transfer(customer2, 4000)

customer1.show_details()
customer2.show_details()
