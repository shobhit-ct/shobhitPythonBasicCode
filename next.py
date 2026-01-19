class mobile:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def verify(self,ver):
        if(self.__pin==ver):
            return"verified"
        else:
          return"inncorrect"
    
j=mobile("VIVO",56)
print(j.verify(56))
print(j.verify(56))
