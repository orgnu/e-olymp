a = int(input())

for t in range(a):
    k = int(input())
    print ("GCVVGCCVG"[(3 * (k % 3)) : (3 * (k % 3) + 3)])