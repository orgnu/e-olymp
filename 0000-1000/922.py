a = int(input())
b = list(map(int,input().split()))
print(b[-1],*b[:-1])