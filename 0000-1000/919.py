a = int(input())
b = [float(i) for i in input().split()]
ucler = []
musbet = []
for i in range(1, len(b)+1):
    if(i % 3 == 0):
        ucler.append(b[i-1])
for i in ucler:
    if(i > 0):
        musbet.append(i)
print(len(musbet), "{:.2f}".format(sum(musbet)))