a = int(input())
b = bin(a)[2:]
for i in range(len(b) - 1):
    b = b[1:] + b[0]
    a = max(a, int(b, 2))
print(a)