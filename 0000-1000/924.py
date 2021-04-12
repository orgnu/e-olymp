a, b = map(float, input().split())
p = 3.141592653589793
S = p*(b**2) - a
R = (S/p)**0.5
print("{:.2f}".format(R))