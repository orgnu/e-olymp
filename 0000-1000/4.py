rbx, rby, rb, rix, riy, ri = map(float, input().split())
d = abs(ri) + abs(rb)
l = ((rbx-rix)**2 + (rby-riy)**2)**0.5
if(rbx == rix and rby == riy and rb == ri):
    print(-1)
else:
    if(d == l):
        print(1)
    elif(d > l):
        print(2)
    else:
        print(0)
