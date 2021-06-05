a = int(input())
n1 = 0
n2 = a-1
for i in range(1, a+1):
    print(n2*"2"+"0"+n1*"1")
    n2 -= 1
    n1 += 1