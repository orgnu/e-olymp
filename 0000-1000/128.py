a = int(input())
b = 0
for i in range(10):
    for j in range(10):
        k = a - i - j
        if 0 <= k <= 9:
            b += 1
print(b*b)