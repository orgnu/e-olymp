a = int(input())

p=a/3
v=a/3
m=a/3
v=v+p/2+m/2
p=p/2
m=m/2
m=m+v/2+p/2
v=v/2
p=p/2
p=p+v/2+m/2
v=v/2
m=m/2

print(int(p),int(v),int(m))