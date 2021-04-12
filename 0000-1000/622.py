a = int(input())
b = bin(a).replace("0b", "")
c = list(str(b))
counter = 0
for i in c:
    if(i == "1"):
        counter += 1
print(counter)