class Encapsulation:
    def __init__(self,a):
        self.a = a
    def public_var(self,b):
        self.b=b
    def protected_var(self,c):
        self._c=c
    def private_var(self,d):
        self.__d=d
        #  the __ double undersocre show private and _c single underscore show protected

e = Encapsulation(50)
e.public_var(60)
e.protected_var(70)
e.private_var(900)

print('Accessing my public_varibalbe',e.b)

print('Accessing my protected_varibalbe',e._c)

print('Accessing my private_varibalbe',e.__d)

