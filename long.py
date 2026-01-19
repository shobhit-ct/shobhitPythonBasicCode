class animal:
    def sound(self):
        print("some genric sound ")

class cat(animal):
     def sound(self):
         print("kukur !")
         
a=animal()
b=cat()
a.sound()
b.sound()