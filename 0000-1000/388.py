a = int(input())
counter = 0
while(a != 1):
    if(a % 2 == 0):
        a = int(a/2)
        counter += 1
    else:
        a = a+1
        counter += 1
print(counter)