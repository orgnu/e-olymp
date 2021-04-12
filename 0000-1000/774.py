r, a, b = map(int, input().split())
d = r*2
if(d >= (a**2+b**2)**0.5):
    print("YES")
else:
    print("NO")