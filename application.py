# Assignment 3
# 2023-12-1
# Jeremy Tica

class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.__accountNumber = accountNumber
        self.__accountHolderName = accountHolderName
        self.__rateOfInterest = rateOfInterest
        self.__currentBalance = currentBalance

    def getAccountNumber(self):
        return self.__accountNumber

    def getAccountHolderName(self):
        return self.__accountHolderName

    def getRateOfInterest(self):
        return self.__rateOfInterest
    
    def getCurrentBalance(self):
        return self.__currentBalance


    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def setAccountHolderName(self, accountHolderName):
        self.__accountHolderName = accountHolderName

    def setRateOfInterest(self, rateOfInterest):
        self.__rateOfInterest = rateOfInterest
    
    def setCurrentBalance(self, currentBalance):
        self.__currentBalance = currentBalance


    def deposit():
        pass

    def withdraw():
        pass


class SavingsAccount(Account):
    def __init__(self):
        super().__init__()


class ChequingAccount(Account):
    def __init__(self):
        super().__init__()



def run():
    showMainMenu()
    showAccountMenu()

def showMainMenu():
    while True:
        user_selection = input("Welcome to the Programming Bank\n\nTo select an option, type in a corresponding number:\n\nOpen Account [1]\nSelect Account [2]\nExit [3]\n\n")
        if user_selection == "1":
            pass
        elif user_selection == "2":
            print("\nShowing Account...\n")
            showAccountMenu()
        elif user_selection == "3":
            print("\nThank you for using Programming Bank!\n")
            exit()
        else:
            print("\nThat is not a valid option.\n")

def showAccountMenu():
    while True:
        user_selection = input("\nCheck Balance [1]\nDeposit [2]\nWithdraw [3]\nExit Account [4]")
        if user_selection == "1":
            Account.getCurrentBalance()
            break
        elif user_selection == "2":
            Account.deposit()
            break
        elif user_selection == "3":
            Account.withdraw()
            break
        elif user_selection == "4":
            showMainMenu()
            break
        else:
            print("\nThat is not a valid option.\n")

#! Program execution
run()