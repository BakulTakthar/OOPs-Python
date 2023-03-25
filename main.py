class Superheroes():
    def __init__(self, name, age, alias, powers):
        self.name = name
        self.age = age
        self.alias = alias
        self.powers = powers
        self.info = [self.name, self.age, self.alias, self.powers]
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
class Avengers():
    def __init__(self, name, max):
        self.name = name
        self.max = max
        self.heroes = []
        
    def add_hero(self, hero):
        
        if len(self.heroes) < self.max:
            self.heroes.append(hero)
            return True
        
        else:
            return False
    
    def mean_age(self):
        sum = 0
        for hero in self.heroes:
            sum += hero.get_age()
            
        return sum // len(self.heroes)
    
    
    
h1 = Superheroes("tony stark", 56, "iron man", "super suit")
h2 = Superheroes("the vision", 14, "the vision", "android abilities")
h3 = Superheroes("stephen strange", 67, "doctor strange", "wizardry")

team = Avengers("avengers", 3)
team.add_hero(h1)
team.add_hero(h2)
team.add_hero(h3)

print(team.heroes[0].info)
print(team.heroes[1].info)
print(team.heroes[2].info)

print(team.mean_age())

print(team.add_hero(h1))

print("hello world")