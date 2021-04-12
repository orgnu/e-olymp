a, b, c = map(float, input().split())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print("{:.2f}".format(2*S/a), "{:.2f}".format(2*S/b), "{:.2f}".format(2*S/c))