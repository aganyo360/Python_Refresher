class Student:
    def __init__(self, name, rollno, gender):
        self.name = name
        self.rollno = rollno
        self.gender = gender
    def display(self):
        print(self.name, self.rollno, self.gender)

print(Student('Brice',1234, 'male').display())

# to make it print in dictinary format user  e.__dict__