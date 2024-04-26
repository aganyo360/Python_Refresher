class Dog():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + " rolled over!")
