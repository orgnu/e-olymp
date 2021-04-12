a = int(input())
b = list(str(a))
c = []
result = 1
for i in b:
    c.append(int(i))
for i in c:
    result = result*i
print(result)