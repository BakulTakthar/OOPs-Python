class Pet: #general class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def intro(self):
        print(f"satsrikaal ji i am {self.name} and i am {self.age} years old")
        
    def speak(self):
        print("bol raha hu me")
        

class Dog(Pet):       # inherits from the general pet class
    def speak(self):
        print("ruff ruff!")
        
        
class Cat(Pet):  
    def speak(self):
        print("meow!")
        
        
c = Cat("billo raani badi seani", 23)
d = Dog("tuhadda kutta tommy", 70)

c.intro()   
c.speak()

'''
in this example of cats and dogs they both printed meow and ruff respectively even tough
there were the function of speak in the general Pet class also because the function of specific
class is given more priority if both functions are same in general and specific class

'''
print("\n\n\n\n\n\n\n\n")    

d.intro()
d.speak()
        
class Fish(Pet): 
    pass      
        
f = Fish("machli jal di rani", 89)
print("\n\n\n\n\n\n\n\n")    
f.intro()
f.speak()
''' 
in the fish example it printed (bol raha hu me) because the command of general class
was the only one and hence, it was the only prioritized one

'''