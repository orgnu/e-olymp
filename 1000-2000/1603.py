a = int(input())
a = abs(a)
b = list(str(a))
c = []
for f in b:
    c.append(int(f))
print(sum(c))