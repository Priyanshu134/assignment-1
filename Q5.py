import math
n=int(input("Enter angle(0-345) to get its sine and cosine"))
a = math.sin(math.radians(n))
b = math.cos(math.radians(n))
print(round(a,4),round(b,4))