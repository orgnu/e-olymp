x1, y1, x2, y2, x3, y3 = map(float, input().split())
a = ((x1-x2)**2+(y1-y2)**2)**0.5
b = ((x2-x3)**2+(y2-y3)**2)**0.5
c = ((x1-x3)**2+(y1-y3)**2)**0.5
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print("{:.4f}".format(p*2), "{:.4f}".format(S))