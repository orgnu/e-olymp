a = int(input())
b = 0
res = 0
b = 0
while (b*b < a):
    b += 1
b = b-1
res += b * (b+1) * 2
res += (a - b*b)*2
res += 1
if (a - b*b > b):
    print(res+1)
else:
    print(res)