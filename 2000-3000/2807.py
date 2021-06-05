n = int(input())
from collections import Counter
a = input()
if(n%2==0):
	print("Ok")
else:
	b =list(str(a))
	y = int(n//2 +1)
	cubs = b[:y]
	res = list((Counter(b)-Counter(cubs)).elements())
	result = list((Counter(cubs)-Counter(res)).elements())
	print(*result)