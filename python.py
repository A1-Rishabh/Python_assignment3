#METHOD OVERRIDING IN PYTHON;
class Appliance:
    def power_on(self):
        print("Turning on the appliance.")

class WashingMachine(Appliance):
    def power_on(self):
        print("Washing Machine starting in wash mode.")

obj = WashingMachine()
obj.power_on()
#METHOD OVERLOADING IN PYTHON;
class MathOps:
    def multiply(self, x=1, y=1, z=1):
        return x * y * z

obj = MathOps()

print(obj.multiply())
print(obj.multiply(4))
print(obj.multiply(4, 5))
print(obj.multiply(4, 5, 6))

#DEFAULT CONSTRUCTOR IN PYTHON;
class Example1:
    def __init__(self):
        print("Default constructor executed")

d = Example1()
#PARAMETERIZED CONSTRUCTOR IN PYTHON;
class Person:
    def __init__(self, fname, height):
        self.fname = fname
        self.height = height

p = Person("Amit", 170)
print(p.fname)
print(p.height)
#CONSTRUCTOR WITH DEFAULT ARGUMENTS IN PYTHON;
class Sample:
    def __init__(self, x=None, y=None):
        print("Values:", x, y)

s1 = Sample(50)
s2 = Sample(50, 100)
