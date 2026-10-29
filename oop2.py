#oop2

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 22/7*self.radius**2

    def perimeter(self):
        return 22/7*self.radius*2

    def print_details(self):
        print(f"Circle radius is {self.radius}, area is {self.area()}, perimeter is {self.perimeter()}, area is {self.area()}")

c1 = Circle(5)
c2= Circle(20)
c3= Circle(40)

print(c1.area())
c1.print_details()

# branches --copy--master main
# feature--
# create new branch --TNT-001-login page, create

# we will learn inheritance in python