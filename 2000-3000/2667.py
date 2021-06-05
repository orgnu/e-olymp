n, m, y, x = map(int, input().split())
a = y-1
b = x - 1
ters = a % 2 != 0
print(a * m + ((m - b - 1) if ters else b))