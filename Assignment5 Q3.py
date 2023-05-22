import math

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

if a+b > c and a+c > b and b+c > a:
    # calculate semi-perimeter
    s = (a + b + c) / 2
    # calculate area using Heron's formula
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle is:", area)
else:
    print("The combination of sides is not possible to form a triangle.")