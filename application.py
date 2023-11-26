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
    pass

def showAccountMenu():
    pass