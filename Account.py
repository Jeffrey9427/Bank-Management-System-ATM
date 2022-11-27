class Account: 
    def __init__(self, balance):
        self.__balance = balance

    def setBalance(self,balance=0):
        if balance > 0:
            self.__balance += balance

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        try:
            if amount > 0:
                self.__balance += amount
                print(f"Transaction completed. Your New Balance: {self.__balance}")
                return True
            else: 
                print(f"Invalid amount transaction aborted")
                return False
        except: 
            print("Invalid input")

    def withdraw(self, amount):
        try: 
            if amount > self.__balance:
                print(f'Your balance is not sufficient. Balance available: {self.__balance}')
                return False
            else: 
                self.__balance -= amount
                print(f"{amount} is debited from your account. Current Balance: {self.__balance}")
                return True
        except:
            print("Invalid input")

    def checkBalance(self):
        print(f"Your current balance is {self.getBalance()}")