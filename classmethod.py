class Employees:
    
    num_leaves = 4
    
    def __init__(self, name, role, salary):
        self.name = name
        self.salary = salary
        self.role = role
        
    def print_details(self):
        print(self.name)
        
        
    @classmethod
    def change_leaves(cls, newleaves):
        cls.num_leaves = newleaves
        
        
    @classmethod 
    def make_data(cls, user_input):
        data = user_input.split("/")
        
        return cls(data[0], data[1], data[2])
        
e1 = Employees("billu", "accountant", 45000 )
e2 = Employees("priti","HR", 65000)

e1.print_details()

e1.change_leaves(30)
print(e2.num_leaves)
# print(Employees.num_leaves)

print(e1.num_leaves)

e3 = Employees.make_data("Jhillu/sales executive/50000")

print(e3.role)