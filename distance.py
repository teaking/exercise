'''Finding distance of two points - pythagorean theorem'''
import math

def main():
    print(distance(1,2,4,6))

def distance(x,y,x1,y1):
    #sqrt((x2 - x1)^2 + (y2 - y1)^2)
    return math.sqrt(math.pow((x1 - x),2) + math.pow((y1 - y),2))


if __name__ == '__main__':
    main()
