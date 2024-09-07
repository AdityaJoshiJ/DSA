# Atm Card Detail's
# 1 user name public
# 2 Password private
# 3 card number protected
# 4 Address public
# 5 Type-> Debit/credit public
# 6 Bank name public
# 7 Mobile Number public
# 8 Balance
# Write a program to build a atm card Detail's using OOPs concept
from abc import ABC, abstractmethod


class Bank(ABC):
    def __init__(self):
        self.username = 'aditya'

    def detail(self):
        self.Uname = input("Enter Your User Name :")
        while self.Uname != self.username:
            self.Uname = input("Enter Your User Name :")
            if self.Uname == self.username:
                self.cardnum = int(input("Insert Card Number :"))
                pass
            else:
                print("Wrong User Name")


obj = Bank()
obj.detail()
