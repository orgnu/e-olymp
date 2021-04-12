a, b, k = map(int, input().split())
print(a//b, end="")
print(".", end="")
d = a % b
i = 0
while(i < k):
    d = d * 10
    print(int(d/b), end="")
    d = d % b
    i += 1