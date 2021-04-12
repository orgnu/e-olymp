a = int(input())
r = list(map(float,input().split()))[:a]
m = []
s = 0
for i in r:
    if(i<0):
        s+=1
        m.append(i)
cem = "{:.2f}".format(sum(m))
print(s,cem)