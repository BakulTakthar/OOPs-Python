print("hello world")
class Calculator:
    def __init__(self, name):
        self.name = name
        print(name)
        
    def add(self, num1, num2):
        return num1 + num2, self.name
    
    def dog(self):
        return "bow bow!", self.name
    
c = Calculator("guddu")

print(c.add(3,5))

c2 = Calculator("duggu")
print(c2.dog())