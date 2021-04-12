a = int(input())
for i in range(0, a):
    b, c = map(float, input().split())
    print("{:.4f}".format(b+c), "{:.4f}".format(b*c))