class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(self.name.title() + " is now walking.")
    
    def eat(self):
        print(self.name.title() + " eating")

class Dog(Animal):
    def __init__(self, name, age, gender):
        '''initialize attributes for the parent class'''
        super().__init__(name, age, gender)

class Cat(Animal):
    def __init__(self, name, age, gender):
        super.__init__(name, age, gender)

first_dog = Dog('Tito', 3, 'male')

first_dog.walk()

first_dog.eat()

print(first_dog.name.title() + " is " + str(first_dog.age) + " years old.")

first_cat = Cat('')