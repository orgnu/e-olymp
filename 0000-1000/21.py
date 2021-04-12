n, p = input().split()
del n
p = float(p)/100
count = list(map(float, input().split()))
count.sort()
while len(count) != 2:
    a = count[0]
    b = count[1]
    del count[0]
    del count[0]
    c = round((a+b)*(1-p), 2)
    count.append(c)
    count.sort()
    del a
    del b
result = (count[1]+count[0])*(1-p)
del count
result = round(result, 2)
print("%.2f" % (result))