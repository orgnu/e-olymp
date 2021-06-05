a = list(map(int,input().split()))
del(a[0])
ma = max(a)
mi = min(a)
result =[]
for i in a:
	if(i==ma):
		result.append(mi)
	else:
		result.append(i)
print(*result)