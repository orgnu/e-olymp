m, n = map(int, input().split())
cemler = []
index = 0
for i in range(m, n+1):
    cemler.append(sum([int(r) for r in str(i)]))
kicik = min(cemler)
for i in cemler:
    if(i == kicik):
        index += 1
print(index)