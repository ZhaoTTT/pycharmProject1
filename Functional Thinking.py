### Functions vs Methods
## Method example
class Car:
    def getAreaMethod(radius):
        pi = 3.14
        area = pi * radius ** 2
        print(area)


car = Car
car.getAreaMethod(10)

## Function example
import math
# using function def
def areaofcircle(radius):
    return math.pi * radius * radius
print(areaofcircle(10))
# using lambda
circlearea = lambda radius:math.pi * radius * radius
print(circlearea(10))