#Helicopter Math Project
from math import cos, tan, atan, radians, degrees, sqrt, pow
def Cos(a):
    return cos(radians(a))
def Tan(a):
    return tan(radians(a))
def Atan(a):
    return degrees(atan(a))

E = float(input("Please input E: "))
A = float(input("Please input A: "))
Z = float(input("Please input Z: "))
Lpos = input("Please input position of L in the form x,y (no parentheses): ")
print("")
print("Results: ")
Lpos = Lpos.split(",")
Lx = float(Lpos[0])
Ly = float(Lpos[1])

TP = (1/(Tan(90-E)))*Z
Px = Cos(A)*TP
Py = Tan(A)*Px
N = Py - Ly
D = Px - Lx
LP = sqrt(D*D + N*N)

AZIM = Atan(N/D)
if D < 0:
    AZIM += 180
if D > 0 and N < 0:
    AZIM += 360
if D == 0 and N > 0:
    AZIM = 90
if D == 0 and N < 0:
    AZIM = 270
if D < 0 and N == 0:
    AZIM = 180
if D > 0 and N == 0:
    AZIM = 0
if D == 0 and N == 0:
    AZIM = "undefined"
print ("AZIM is " + str(AZIM))

ELEV = 90 - Atan((Z-61)/LP)
print ("ELEV is " + str(ELEV))

Range = sqrt(LP*LP + (Z-61)*(Z-61))
print ("Range is " + str(Range))