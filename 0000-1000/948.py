import math
d, p = map(int,input().split())
sahe = d*(d+math.sqrt(4*p*p-d*d))
hecm =d*d*math.sqrt(p*p-d*d/2)/3
print("{:.3f}".format(sahe),end=" ")
print("{:.3f}".format(hecm))