a = int(input())
counter = 0
for i in range(1, a):
    if(a % i == a//i):
        counter += 1
print(counter)