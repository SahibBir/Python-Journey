"""
Submitted By: SAHIB BIR SINGH BHATIA
Student ID: 201547831
COMP 517 - Assignment 3 - 2020-21 - JAN21 - CA Assignment 3 - BANK ACCOUNTS
"""

# Importing Random and Datetime modules
import random
from datetime import datetime


class BasicAccount(object):  # Basic Account class
    """acNum – the number of the account."""
    acNum: int = 0

    """__init__(self, str, float)"""

    def __init__(self, acName: str, openingBalance: float):
        self.name: str = acName
        print("Hi {}, Welcome to Goliath National Bank Family.\n".format(self.name))
        if type(openingBalance) == str or openingBalance < 0:
            print("Please enter valid value for balance and try again\n")
        else:
            self.balance = openingBalance
            self.cardNum: str = ""
            self.cardExp: (int, int) = ()
            BasicAccount.acNum = BasicAccount.acNum + 1  # incrementing acNum by 1 to initialise account number
            self.acNum = BasicAccount.acNum
            self.accClosed: bool = False
            self.accExist: bool = True

    """__str__"""

    def __str__(self):
        if self.accClosed:   # checking if account is closed or not
            return "This account was closed\n"
        else:
            return "{} has balance £{} with no overdraft\n".format(self.name, round(self.balance), 2)

    """deposit(self,float)"""

    def deposit(self, amount: float):
        if self.accClosed:  # checking if account is closed or not
            return "This account was closed\n"
        else:
            if amount < 0:  # checking if valid input deposit amount is provided
                print("Please try again with valid value. [Deposit amount cannot be negative!]\n")
            else:
                self.balance = self.balance + amount    # updating balance
                print("You have successfully deposited £{} in account {}. Your balance is £{}\n"
                      .format(amount, self.acNum, round(self.balance), 2))

    """withdraw(self,float)"""

    def withdraw(self, amount: float):
        if self.accExist:  # checking if account exists and valid input withdraw amount is provided
            if self.balance < amount:     # checking if enough balance is present for withdrawal of requested amount
                print("Can not withdraw £{}\n".format(amount))
            elif amount < 0:  # checking if valid input withdraw amount is provided
                print("Invalid amount requested for withdrawal.[Amount cannot be negative]\n")
            else:
                if self.accClosed:   # checking if account is closed or not
                    print("Thank you for choosing us.Please collect your balance £{}\n".format(round(self.balance, 2)))
                else:
                    self.balance = self.balance - amount   # updating balance
                    print("{0} has withdrew £{1}. New balance is £{2}\n".format(self.name, amount,
                                                                                round(self.balance, 2)))
        else:
            print("This account was closed.Cannot withdraw anymore\n")

    """getAvailableBalance(self)"""

    def getAvailableBalance(self) -> float:
        if self.accClosed:  # checking if account is closed or not
            print("This account was closed\n")
        else:
            return round(self.balance, 2)

    """getBalance(self)"""

    def getBalance(self) -> float:
        if self.accClosed:  # checking if account is closed or not
            print("This account was closed\n")
        else:
            return round(self.balance, 2)

    """printBalance(self)"""

    def printBalance(self):
        if self.accClosed:  # checking if account is closed or not
            print("This account was closed\n")
        else:
            print("You have balance: £{}\nOverdraft is not available\n".format(round(self.balance), 2))

    """getName(self)"""

    def getName(self) -> str:
        if self.accClosed:  # checking if account is closed or not
            print("This account was closed\n")
        else:
            return "This account belongs to {}\n".format(self.name)

    """getAcNum(self)"""

    def getAcNum(self) -> str:
        if self.accClosed:  # checking if account is closed or not
            print("This account was closed\n")
        else:
            return "Hi {0}, Your Account number is {1}\n".format(self.name, self.acNum)

    """issueNewCard(self)"""

    def issueNewCard(self):
        if self.accClosed:  # checking if account is closed or not
            print("This account was closed\n")
        else:
            lis = []  # Creating an empty list
            for i in range(0, 17):
                n = random.randint(0, 9)
                lis.append(str(n))   # Adding elements in the list
            self.cardNum = ''.join(lis)  # Creating the card number
            month = int(datetime.today().strftime("%m"))
            year = datetime.today().strftime("%Y")
            year = int(year[2:]) + 3
            self.cardExp = (month, year)   # Creating expiry date

    """getCardDetails(self)"""

    def getCardDetails(self) -> str:
        if self.accClosed:  # checking if account is closed or not
            print("This account was closed")
        else:
            return "Hi {0}, Your new card number is {1}-{2}-{3}-{4} and it expires on {5}\n".format(self.name,
                                                                                                    self.cardNum[:4],
                                                                                                    self.cardNum[5:9],
                                                                                                    self.cardNum[9:13],
                                                                                                    self.cardNum[13:17],
                                                                                                    self.cardExp)

    """closeAccount(self)"""

    def closeAccount(self) -> bool:
        if self.balance == 0:  # checking if balance is zero
            print("You don't have any balance. Thank you for choosing us. We hope to see you again.\n")
        else:
            self.accClosed = True  # Closing account
            self.withdraw(self.balance)
        self.accExist = False    # Account status
        return self.accClosed


class PremiumAccount(BasicAccount):  # Premium Account class
    """__init__(self,str,float,float)"""

    def __init__(self, acName: str, openingBalance: float, initialOverdraft: float):
        super().__init__(acName, openingBalance)
        if type(initialOverdraft) == str or initialOverdraft < 0:
            print("Please enter valid initialOverdraft value.\n")
        else:
            self.overdraftLimit: float = initialOverdraft
            self.overdraft: bool = False
            self.usableOverdraft: float = initialOverdraft

    """__str__"""

    def __str__(self):
        if self.accClosed:  # checking if account is closed or not
            return "This account was closed\n"
        else:
            return "{} has balance £{} with an overdraftLimit of £{}\n".format(self.name, round(self.balance, 2),
                                                                               round(self.overdraftLimit), 2)

    """setOverdraftLimit(self, float)"""

    def setOverdraftLimit(self, newLimit: float):
        self.overdraftLimit = newLimit   # initialising overdraft limit to new limit
        print("Overdraft Limit is now set to £{}\n".format(round(self.overdraftLimit, 2)))

    """deposit(self,float)"""

    def deposit(self, amount: float):
        if self.accClosed:  # checking if account is closed or not
            print("This account was closed.Cannot deposit anymore\n")
        elif self.overdraft and amount >= 0:  # checking if account is overdrawn and amount is valid input
            diff = self.overdraftLimit - self.usableOverdraft
            x = amount - diff
            self.balance = self.balance + x     # updating balance
            self.usableOverdraft = self.usableOverdraft + (amount - x)   # updating usable overdraft
            self.overdraft = False   # updating status of whether account is overdrawn or not
            print("You hve successfully deposited £{0} in account {1}. Your current balance is £{2} and Available "
                  "overdraft is £{3}\n"
                  .format(amount, self.acNum, round(self.balance, 2), round(self.usableOverdraft), 2))
        elif amount >= 0:  # checking if amount is valid input
            self.balance = self.balance + amount  # updating balance
            print("You have successfully deposited £{0} in account {1}. Your balance is £{2}\n"
                  .format(amount, self.acNum, round(self.balance), 2))
        else:
            print("Invalid amount requested for deposit.[Deposit cannot be negative!]\n")

    """withdraw(self,float)"""

    def withdraw(self, amount: float):
        if self.accExist and amount >= 0:  # checking if account exists and amount is valid input
            if self.balance + self.usableOverdraft < amount:  # checking if account contains enough balance
                print("Can not withdraw £{}".format(amount))
            elif self.balance >= amount and not self.accClosed:  # checking if balance is enough and account not closed
                self.balance = self.balance - amount  # updating balance
                print("{0} has withdrew £{1}. New balance is £{2} and available overdraft is £{3}\n"
                      .format(self.name, amount, round(self.balance, 2), round(self.usableOverdraft, 2)))
            else:
                if self.accClosed:
                    print("Thank you for choosing us.Please collect your balance £{}\n".format(round(self.balance), 2))
                else:
                    y = amount - self.balance
                    self.balance = self.balance - amount  # updating balance
                    self.usableOverdraft = self.usableOverdraft - y  # updating usable overdraft
                    self.overdraft = True  # updating overdrawn account status
                    print("{0} has withdrew £{1}. New balance is £{2} and available overdraft is £{3}\n"
                          .format(self.name, amount, round(self.balance, 2), round(self.usableOverdraft, 2)))
        elif amount < 0:  # checking if amount requested is a valid input
            print("Invalid amount requested for withdrawal.[Amount cannot be negative!]\n")
        else:
            print("This account was closed.Cannot withdraw anymore\n")

    """getAvailableBalance"""

    def getAvailableBalance(self) -> float:
        if self.accClosed:   # checking if account is closed or not
            print("This account was closed\n")
        else:
            return round(self.balance + self.usableOverdraft, 2)

    """printBalance"""

    def printBalance(self):
        if self.accClosed:   # checking if account is closed or not
            print("This account was closed\n")
        else:
            totalBalance = round(self.balance + self.usableOverdraft, 2)
            print("Your total balance is : £{0}\nUsable overdraft amount is: £{1}\nAccount Balance is :£{2}\n"
                  .format(totalBalance, round(self.usableOverdraft, 2), round(self.balance)))

    """closeAccount"""

    def closeAccount(self) -> bool:
        if self.overdraft:   # checking if account is overdrawn
            print("Can not close account due to customer being overdrawn by £{}\n"
                  .format(round(self.overdraftLimit - self.usableOverdraft, 2)))
        else:
            self.accClosed = True  # updating close account status
            if self.balance == 0:
                print("You don't have any balance. Thank you for choosing us. We hope to see you again.\n")
            else:
                self.withdraw(self.balance)
        self.accExist = False  # updating account existence status
        return self.accClosed
