class Person:
    number_of_people = 4
    
    def __init__(self, name):
        self.name = name 
        Person.number_of_people += 1
# Person.number_of_people = 34        
        
p1 = Person("bakul")
p2 = Person("aadu paadu")

print(Person.number_of_people)