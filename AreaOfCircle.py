# Python code to find the area of a circle

def area(r):
    print("Radius entered: ",r)
    pi = 3.14
    area = pi * (r**2)
    return area

radius = float(input("Enter the radius of the circle: "))
print("Area of circle is: ", area(radius))
