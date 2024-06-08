class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(self.name.title() + " is now walking.")
    
    def eat(self):
        print(self.name.title() + " eating")

my_cow = Animal('Bonito', 23, 'female')

my_cow.walk()
my_cow.eat()