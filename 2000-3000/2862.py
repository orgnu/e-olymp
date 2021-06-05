a = int(input())
c = (a//2) + 1
b = 1
for i in range(1, c):
    if(a % i == 0):
        b += 1
print(b)