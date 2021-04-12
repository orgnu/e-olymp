a = input()
b = len(a)
result = 0
if(int(b) % 2 == 1):
    result += 1
for i in range(0, int(b)//2):
    if(a[i] == a[b-(i+1)]):
        result += 1
print(result)