# inserting a string in the middle of another string
def insert_in_middle(original, to_insert):
    mid = len(original) // 2
    return original[:mid] + to_insert + original[mid:]
s1= input("enter a string ")
s2= input("enter a string ")
print("result:",insert_in_middle(s1,s2))


# calculating area using functions 
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_square(side):
    return side ** 2

def area_of_trapezoid(a, b, height):
    return 0.5 * (a + b) * height

print("Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
print("4. Square")
print("5. Trapezoid")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    r = float(input("Enter radius: "))
    print(f"Area of Circle = {area_of_circle(r):.2f}")

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print(f"Area of Rectangle = {area_of_rectangle(l, w):.2f}")

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print(f"Area of Triangle = {area_of_triangle(b, h):.2f}")

elif choice == 4:
    s = float(input("Enter side: "))
    print(f"Area of Square = {area_of_square(s):.2f}")

elif choice == 5:
    a = float(input("Enter first parallel side: "))
    b = float(input("Enter second parallel side: "))
    h = float(input("Enter height: "))
    print(f"Area of Trapezoid = {area_of_trapezoid(a, b, h):.2f}")

else:
    print("Invalid choice!")