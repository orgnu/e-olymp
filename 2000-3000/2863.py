a = int(input())
b = range(1, a+1)
result = []
for c in b:
    if(a % c == 0 and c % 2 == 1):
        result.append(c)
print(*result, sep="\n")