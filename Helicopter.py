#Helicopter Math Project
from math import cos, tan, atan, radians, degrees, sqrt
def Cos(a):
    return cos(radians(a))
def Tan(a):
    return tan(radians(a))
def Atan(a):
    return degrees(atan(a))

E = float(input("Please input E: "))
A = float(input("Please input A: "))
if A >= 180:
    A -= 180
if A >= 270:
    A -= 90
Z = float(input("Please input Z: "))
Lpos = input("Please input position of L in the form x,y (no parentheses): ")
print("")
print("Results: ")
Lpos = Lpos.split(",")
Lx = float(Lpos[0])
Ly = float(Lpos[1])

TP = (1/(Tan(90-E)))*Z
Px = Cos(A)*TP
Py = sqrt(TP*TP - Px*Px)
LPy = Py - Ly
LPx = Px - Lx
LP = sqrt(LPx*LPx + LPy*LPy)

AZIM = Atan(LPy/LPx)
if A >= 90:
    AZIM += 180
if A >= 180:
    AZIM += 90
if A >= 270:
    AZIM += 90
if AZIM >= 360:
    AZIM -= 360
print ("AZIM is " + str(AZIM))

ELEV = 90 - Atan((Z-61)/LP)
print ("ELEV is " + str(ELEV))

Range = sqrt(LP*LP + (Z-61)*(Z-61))
print ("Range is " + str(Range))
