from Account import *
from Customer import *
from Bank import *

class ATM: 

    no_of_cust = 0

    def __init__(self, data):                           # ATM would accept list of datas of customers' detail
        self.__data = data

        self.__userIndex = None
        
        self.__bank = Bank("Jeffrey's Bank")            # creating a bank named Jeffrey's Bank
        for index, data in enumerate(self.__data):
            self.__bank.addCustomer(data['fName'], data['lName'], data['pin'])       # adding the customer into the bank
            self.__bank.getCustomers(index).setAccount(Account(data['balance']))     # update the customer's balance

        self.__mainMenu()

    def __mainMenu(self):           # menu of ATM system
        notExit = True
        while notExit:
            try:
                print("\nWelcome to Jeffrey's Bank!")
                print("-"*20)
                print("Please choose your role: ")
                print("1. Administrator")
                print("2. Customer")
                print("3. Exit")
                choice = int(input("\nChoose your option: "))
                notExit = self.__runMainMenu(choice)
            except:
                print("Please enter a valid option.")

    def __runMainMenu(self,choice):
        notExit = True
        while notExit: 
            if choice == 1:
                if self.__adminAuthentication() == True:        # will ask for admin's authorize (pin)
                    self.__adminMenu()                          # if true, will go to admin menu
                return True
            elif choice == 2:
                if self.__customerAuthentication() == True:     # will ask for customer' authorize (name and pin)
                    self.__customerMenu()                       # will show customer menu if authorized
                return True
            elif choice == 3: 
                notExit = False         # stop the loop from running main menu
                print("Thank you for using Jeffrey's Bank. See you again :)")
                return False            # stop the process of ATM System
    

# ADMINISTRATOR
    def __adminAuthentication(self):         # authentication for admin login
        adminPin = input(">> PIN : ")
        while not self.__adminPin(adminPin):
            print("Wrong pin number! Please re-enter pin")
            adminPin = input(">> PIN : ")

    def __adminPin(self,adminPin):      # check credential for pin 
        if adminPin == "ASDF2345":
            self.__adminMenu()          # if true, will show admin menu
            return True
        return False

    def __adminMenu(self):               # after login, admin can choose what they can do
        notExit = True
        while notExit: 
            try:
                print("")
                print('-'*20)
                print("What you want to do: ")
                print("1. Add Customer")
                print("2. Delete Customer")
                print("3. Edit Customer")
                print("4. Search Customer")
                print("5. Exit")
                print("-"*20)
                option = int(input("\nChoose your option: "))
                notExit = self.__runAdminMenu(option)
            except ValueError:
                print("Please enter a valid option.")

    def __runAdminMenu(self, option):
        loop = 1
        while loop == 1:
            if option == 1:                  # add customer 
                fName = input("\nFirst Name: ")
                lName = input("Last Name: ")
                pin = input("Pin: ")
                balance = input("Balance: ")

                self.__data.append(
                    {
                        'fName': fName,
                        'lName': lName,
                        'pin' : pin,
                        'balance': int(balance)
                    }
                )
                self.__bank.addCustomer(fName, lName, pin)      # add the customer detail into the bank
                self.__bank.getCustomers(len(self.__data)-1).setAccount(Account(int(balance)))      # update the customer's balance into the bank
                print(f"Customer {fName} {lName} has been added successfully.")
                return True

            elif option == 2:                  # delete customer 
                for i in range(0, len(self.__data)):
                    print(f"{i+1}. Customer: {self.__data[i]['fName']} {self.__data[i]['lName']}")      # printing the list of customers before we decided which one to delete

                delete = int(input("\nWhich customer index do you want to delete?: "))

                if delete > len(self.__data):
                    print(f"There are only {len(self.__data)} customers. Please enter a proper value!")     
                else:
                    print(f"Customer {self.__data[delete-1]['fName']} {self.__data[delete-1]['lName']} has been deleted successfully")
                    del self.__data[delete-1]

                return True

            elif option == 3:                   # edit customer
                for i in range(0, len(self.__data)):
                    print(f"{i+1}. Customer: {self.__data[i]['fName']} {self.__data[i]['lName']}")      # printing the list of customers before we decided which one to edit

                edit = int(input("\nWhich customer index do you want to edit?: "))

                if edit > len(self.__data):
                    print(f"There are only {len(self.__data)} customers. Please enter a proper value!")
                else:
                    print("\nNew Customer Details: ")
                    fName = input("First Name: ")
                    lName = input("Last Name: ")
                    pin = int(input("Pin : "))
                    balance = int(input("Balance: "))

                    print(f"Customer details of {self.__data[edit-1]['fName']} {self.__data[edit-1]['lName']} has been changed successfully")
                    self.__data[edit-1] = {
                        'fName': fName,
                        'lName': lName,
                        'pin': pin,
                        'balance': balance
                    }

                return True

            elif option == 4:                    # search customer
                for index, data in enumerate(self.__data):
                    print(f"\nCustomer {(index+1)}: ")
                    print(f"First Name: {data['fName']}")
                    print(f"Last Name: {data['lName']}")
                    print(f"Pin: {data['pin']}")
                    print(f"Balance: {data['balance']}\n")
                return True

            elif option == 5:                   # exit, return false and back to main page
                loop = 0 
                print("Thank you for your hard work. See you again! :)")
                return False
    
# CUSTOMER

    def __customerAuthentication(self):             # authentication for customer login
        credFirstName = input("First Name: ")
        credLastName = input("Last Name: ")
        credPin = input("Pin : ")

        while not self.__checkCredentialNames(credFirstName, credLastName, credPin):    
            print("Wrong credential! Please re-enter your credential.")
            credFirstName = input("First Name: ")
            credLastName = input("Last Name: ")
            credPin = input("Pin: ")

        return True             # will show customer menu if true

    def __checkCredentialNames(self, fName, lName, pin):
        for index, data in enumerate(self.__data):
            if fName == data['fName'] and lName == data['lName'] and pin == data['pin']:        # when all the credentials is correct
                self.__userIndex = index
                return True

        return False

    def __customerMenu(self):               # after log in, customer can choose what they can do
        notExit = True
        while notExit: 
            try: 
                print("\nPlease choose one of the following options")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Log out")
                option = int(input("Choose your option: "))
                notExit = self.__runCustomerMenu(option)
            except: 
                print("Please enter a valid option \n")

    def __runCustomerMenu(self, option):
        loop = 1
        while loop == 1:
            while option not in range(1,5):
                print("Please try again.")
                option = int(input("Choose your option: "))
            if option == 1:             # check balance
                self.__bank.getCustomers(self.__userIndex).getAccount().checkBalance()
                return True

            elif option == 2:           # deposit
                amount = int(input("How much $$ you would like to deposit: "))
                self.__bank.getCustomers(self.__userIndex).getAccount().deposit(amount)
                return True

            elif option == 3:           # withdraw
                amount = int(input("How much $$ you would like to withdraw: "))
                self.__bank.getCustomers(self.__userIndex).getAccount().withdraw(amount)
                return True

            elif option == 4:           # log out from customer mneu 
                loop = 0
                print("Thank you for using our ATM, see you again!")
                return False            # back to main menu page


