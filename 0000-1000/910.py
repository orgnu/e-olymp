a = int(input())
r = list(map(float,input().split()))[:a]
m = []
for i in r:
    if(i>0):
        m.append(i)
    else:
        pass
s = len(m)
cem = (sum(m))
tcem = int(cem)
if(s==0):
    print("Not Found")
else:
    if(cem - tcem == 0.0):
        print(tcem/s)
    else:
        print("{:.2f}".format(cem/s))