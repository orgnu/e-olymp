a = int(input())
r = list(map(int,input().split()))[:a]
cavab = []
for i in r:
    if(i<0):
        cavab.append(i)
    else:
        cavab.append(i+2)
print (*cavab, sep=" ")