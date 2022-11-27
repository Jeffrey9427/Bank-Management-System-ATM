from Customer import Customer
from Account import Account

class Bank():
    def __init__(self, bName):
        self.__bName = bName
        self.__customers = []
        self.__numOfCustomers = 0

    def setbName(self,bName):
        self.__bName = bName

    def getbName(self):
        return self.__bName

    def addCustomer(self, fName, lName, pin):
        self.__customers.append(Customer(fName, lName, pin))
        self.__numOfCustomers += 1

    def getCustomers(self, index):
        return self.__customers[index]

    def getNumOfCustomers(self):
        return self.__numOfCustomers