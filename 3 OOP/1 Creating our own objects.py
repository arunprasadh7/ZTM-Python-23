# Creating our own objects

class PlayerCharacter:
    steam_account = True  # class attributes

    def __init__(self, name, age):
        self.name = name  # instance attributes
        self.age = age

    def greet(self):
        # return 'Hello ! Have a good day!'
        return self

    @classmethod
    def add_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def add_things2(num1, num2):
        return num1 + num2


p1 = PlayerCharacter('Arun', 26)
p2 = PlayerCharacter('Storm', 100)

print(p1.name)
print(p1.age)
print(p1.greet())

print(p2.name)
print(p2.age)
print(p2.greet())

print(p1.add_things(5, 5))

# We can directly access class methods using class names
# classmethods can be used even if instance is not created
print(PlayerCharacter.add_things(2, 2))

# staticmethod - does not get access to class attributes
print(PlayerCharacter.add_things2(6, 6))


print(p1.greet().greet())


# polymorphism

class first:
    def name(self):
        print('First name')


class last:
    def name(self):
        print('Second name')


c1 = first()
c2 = last()

c1.name()
c2.name()


# abstraction eg 2

class dog:
    legs = 4

    def color(self):
        print('This breed is available in multi colors')


class doberman(dog):
    def color(self):
        print('This breed is available in black and brown shades.')


class dalmation(dog):
    def color(self):
        print('This breed is available in white with dark spots')


d1 = dog()
d2 = doberman()
d3 = dalmation()

d1.color()
d2.color()
d3.color()

print(d1.legs)
print(d2.legs)
print(d3.legs)


# Super function

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


class Square(Rectangle):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def area(self):
        a = self.length * self.breadth
        return a


class Cube(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())


# eg 2
class Cat:
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age


class BengalCat(Cat):
    def __init__(self, breed, color, age, coat):
        super().__init__(breed, color, age)
        self.coat = coat

    def description(self):
        specs = f'This is a {self.age} month old {self.color} {self.breed} {self.coat} kitten.'
        return specs


class Persian(Cat):
    def __init__(self, breed, color, age, availability):
        super().__init__(breed, color, age)
        self.availability = availability

    def specs(self):
        return f'This is a {self.age} month old {self.color} {self.breed} kitten.\nAvailability = {self.availability}.'


b1 = BengalCat('Bengalcat', 'Spotted brown', 6, 'shortcoat')
print(b1.description())

p1 = Persian('Persian', 'white', 9, 'Unavailable')
print(p1.specs())
