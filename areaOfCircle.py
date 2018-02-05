'''taking two points, center of the circle and a point on the permiter, compute the are 
of circle'''
from distance import distance
import math
def main():
    print(areaOfCircle(distance(0,0,2,2)))

def areaOfCircle(radius):
    #A = pir**2
    return math.pi * (radius**2)

main()
