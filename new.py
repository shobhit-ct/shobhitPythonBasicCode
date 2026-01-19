class bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance #private attribute

    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
            return self.__balance
acc=bankaccount("kallu",524615852145524558)
acc.deposite(5265489524)
print(acc.get_balance())