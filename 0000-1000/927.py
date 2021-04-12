d = int(input())
say = []
for i in range(0,d):
    x,y = map(float,input().split())
    if(y<50.00):
        say.append(x)
print(int(sum(say)))