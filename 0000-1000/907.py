a = int(input())
b = map(float, input().split())
s = 0
for i in b:
    s = s + 1
    if(i <= 2.5):
        print(s, "{:.2f}".format(i))
        break
else:
    print("Not Found")