ff=1
n=int(input())

for i in range(1,2001):
    ff=ff*i
    if ff==n:
        print(i)