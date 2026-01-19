class student:
    def __init__(self,name,salary):
        self.name=name
        self.__balance=salary
    def update(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
st=student("the rock",564228948248)
st.update(516568268)
print(st.get_balance())