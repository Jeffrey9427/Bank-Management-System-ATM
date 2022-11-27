from Account import Account 


class Customer():

    no_of_cust = 0

    def __init__(self, fname, lname, pin):
        self.__fName = fname
        self.__lName = lname
        self.__pin = pin

        Customer.no_of_cust = Customer.no_of_cust + 1

    def setPin(self, pin):
        self.__pin = pin

    def setAccount(self, account):
        self.__account = account

    def getFirstName(self):
        return self.__fName

    def getLastName(self):
        return self.__lName

    def getPin(self):
        return self.__pin

    def getAccount(self):
        return self.__account