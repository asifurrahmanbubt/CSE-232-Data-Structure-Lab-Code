import math
a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))
c = float(input("Enter the value of C: "))
d = (b ** 2) - (4 * a * c)
if d > 0:
x1 = (-b - math.sqrt(d)) / (2 * a)
x2 = (-b + math.sqrt(d)) / (2 * a)
print("x1:", x1)
print("x2:", x2)
elif d == 0:
x = -b / (2 * a)
print("UNIQUE SOLUTION:", x)
else:
print("NO REAL SOLUTION")
