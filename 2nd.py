class mobile:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    def update(self,price):
        self.__price=price
    def display(self):
        return self.__price
j=mobile("VIVO",56000)
j.update(59624)
print(j.display())
