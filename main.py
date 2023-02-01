print("hello world")
class Calculator:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def add(self, num1, num2):
        return num1 + num2, self.name
    
    def get_name(self):
        return self.name
    
    def new_name(self, name):
        self.name = name
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
        
c = Calculator("guddu", 67)

print(c.get_age())
print(c.get_name())

print(".... \n\n\n\n\n .....")

c.set_age(69)
c.new_name("yo mama")
print(c.get_age())
print(c.get_name())