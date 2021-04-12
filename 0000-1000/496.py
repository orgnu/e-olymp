n = int(input())
for i in range(n):
    a, b = input().split()
    a = sorted(a.lower())
    b = sorted(b.lower())
    if(a==b):
        print ("Yes")
    else:
        print("No")