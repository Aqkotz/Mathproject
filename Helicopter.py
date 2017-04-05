#Helicopter Math Project
from math import sin, cos, tan, atan, acos, asin, radians, degrees
def Cos(a):
    return cos(radians(a))
def Sin(a):
    return sin(radians(a))
def Tan(a):
    return tan(radians(a))
def Atan(a):
    return degrees(atan(a))
def Asin(a):
    return degrees(asin(a))
def Acos(a):
    return degrees(acos(a))

E = float(input("Please input E: "))
A = float(input("Please input A: "))
Z = float(input("Please input Z: "))
Lpos = input("Please input position of L in the form x,y (no parentheses): ")
Lpos = Lpos.split(",")
Lx = float(Lpos[0])
Ly = float(Lpos[1])

TP = (1/(Tan(90-E)))*Z
vertT = Atan((Z-61)/TP)
