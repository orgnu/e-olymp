a = int(input())
if(a==0):
    print("Ooops!")
elif(a==1):
    x = int(input())
    print("Ooops!")
else:
    r = list(map(int,input().split()))[:a]
    print(min(r), max(r))