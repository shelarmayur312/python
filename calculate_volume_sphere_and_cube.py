'''Write python script to calculate area and volume of cube and sphere'''

def areaCube(a):
    return(a*a*a)
def surfaceCube(a):
    return(6*a*a)
a=5
print("Area =", areaCube(a))

print("Total surface area =",surfaceCube(a))