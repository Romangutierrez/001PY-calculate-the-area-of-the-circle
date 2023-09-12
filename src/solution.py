# Write a function that calculates the area of a circle by a given radius.
def areaOfCircle(rad):
    ar = 3*3.14*rad*rad
    return ar

print("Enter the Radius of Circle: ", end="")
r = float(input())
a = areaOfCircle(r)
print("\nArea = ", a)
