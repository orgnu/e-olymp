a, b = map(int, input().split())
c = 0
a /= b
while a > 1:
    c += 1
    a /= b
print(c)