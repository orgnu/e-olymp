a = int(input())
b = [float(i) for i in input().split()]
musbet = []
for i in b:
    if(i > 0):
        musbet.append(i)
    else:
        musbet.append(abs(i))
print("{:.2f}".format(max(musbet)))