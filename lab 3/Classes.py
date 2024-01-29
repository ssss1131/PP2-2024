from math import sqrt


# 1
class String:
    def __init__(self):
        self.x = ""

    def getString(self):
        self.x = input()

    def printString(self):
        print(self.x.upper())


# x = String()
# x.getString()
# x.printString()

# 2
class Shape:
    def area(self):
        print(0)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)


'''
cube=Shape()
cube.area()
cube_2=Square(5)
cube_2.area()
'''


# 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)


# t=Rectangle(2,3)
# print(t.area())

# 4
class Points():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"coordinates({self.x};{self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, second_points):
        return sqrt((self.x - second_points.x) ** 2 + (self.y - second_points.y) ** 2)


'''
a=Points(3,3)
b=Points(5,5)
a.show()
b.move(0,1)
b.show()
print(a.dist(b))
'''


# 5
class Bank_Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"New balance {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Your balance {self.balance} and you cant earn your money")
        else:
            self.balance -= money
            print(f"New balance {self.balance}")


'''
a=Bank_Account("Saulet",10000)
a.deposit(100)
a.withdraw(10000)
a.withdraw(200)
'''

# 6
prime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

all_prime = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x > 1, prime))

print(all_prime)

