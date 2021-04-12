a = int(input())
b = [float(i) for i in input().split()]
c = []
for i in b:
    if(i % 6 == 0 and i > 0):
        c.append(i)
print(len(c), int(sum(c)))