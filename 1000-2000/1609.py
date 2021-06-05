a = int(input())
a = abs(a)
l = int(input())
b = list(str(a))
count = 0
for i in b:
    if(int(i)==l):
        count+=1
print(count)