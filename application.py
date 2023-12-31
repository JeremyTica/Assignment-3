# Assignment 3
# 2023-12-1
# Jeremy Tica
import os
class Program:
    def __init__():
        def run():
            dfshowMainMenu()
            showAccountMenu()

def showMainMenu():
    while True:
        user_selection = input("Welcome to the Programming Bank\n\nTo select an option, type in a corresponding number:\n\nOpen Account [1]\nSelect Account [2]\nExit [3]\n\n")
        if user_selection == "1":
            os.system('cls')
            new_account_number()    
        elif user_selection == "2":
            os.system('cls')
            showAccountMenu()
        elif user_selection == "3":
            print("\nThank you for using Programming Bank!\n")
            exit()
        else:
            os.system('cls')
            print("\nThat is not a valid option.\n")
class Bank:
    def __init__(self):
        self.__bankName = "The Greatest Bank"
        self.__list_of_accounts = []
    
    def openAccount():
        pass

    def searchAccount():
        pass
class Account(Bank):
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


    def deposit(self, intended_deposit):
        self.__currentBalance += intended_deposit

    def withdraw(self, intended_withdrawal):
        self.__currentBalance -= intended_withdrawal
        if self.__currentBalance < 0:
            self.__currentBalance += intended_withdrawal
            print("Cannot make transaction. Invalid funds.")


class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.__minimum_balance = 5000
    
    def savings_withdraw(self):
        if self.__currentBalance < self.__minimum_balance:
            return False




class ChequingAccount(Account):
    def __init__(self):
        super().__init__()


list_of_accounts = []
account_numbers = []

def showAccountMenu():
    account_menu = False
    show_existing_accounts = False
    choose_existing_account = False

    if list_of_accounts == []:
        os.system('cls')
        print("\nThere are no existing accounts\n")
    else:
        print("\nShowing Existing Account(s)...\n")
        show_existing_accounts = True

    while show_existing_accounts:
        for existing_accounts in list_of_accounts:
            account_numbers.append(existing_accounts.getAccountNumber())
            print("Bank Account: ", existing_accounts.getAccountNumber())
            index_number = list_of_accounts.index(existing_accounts)

        choose_existing_account = True
        show_existing_accounts = False

    while choose_existing_account:
        existing_account = input("\nPlease select an existing account by inputting the account number: \n\n")
        for existing_accounts in list_of_accounts:
            if existing_account == existing_accounts.getAccountNumber():
                account_menu = True
                choose_existing_account = False
            else:
                print("\nThat account does not exist!\n")

    while account_menu:
        user_selection = input("\nCheck Balance [1]\nDeposit [2]\nWithdraw [3]\nExit Account [4]\n\n")
        if user_selection == "1":
            print("\nCurrent Balance: $ "+ str(list_of_accounts[index_number].getCurrentBalance()) + "\n")
            break
        elif user_selection == "2":
            intended_deposit = float(input("Please input your desired amount to be deposited: "))
            deposit = list_of_accounts[index_number].deposit(intended_deposit)
            print("$" + str(deposit) + " has been deposited.")
            break
        elif user_selection == "3":
            intended_withdrawal = float(input("Please input your desired amount to be withdrawn: "))
            withdrawal = list_of_accounts[index_number].withdraw(intended_withdrawal)
            print("$" + str(withdrawal) + "has been withdrawn.")
            break
        elif user_selection == "4":
            showMainMenu()
            break
        else:
            os.system('cls')
            print("\nThat is not a valid option.\n")

def new_account_number():
    while True:
        global account_number
        account_number = input("Input a new account number formatted XXXXX all numbers: ")
        if account_number.isnumeric() and len(account_number) == 5:
            new_account_holder_name()
            break
        else:
            print("Please input a valid format")

def new_account_holder_name():
    while True:
        global holder_name
        holder_name = input("Input a new holder name: ")
        new_account_rate_of_interest()
        break
        
def new_account_rate_of_interest():
    while True:
        global rate_of_interest
        rate_of_interest = input("Input a rate of interest: ")
        try:
            float(rate_of_interest)
            new_account()
            break
        except ValueError:
            print("Please input a valid format")

def new_account():
    account = Account(account_number, holder_name, rate_of_interest, 0)
    list_of_accounts.append(account)
    os.system('cls')
    print("\nAccount Successfully Created\n")

#! Program execution
run()