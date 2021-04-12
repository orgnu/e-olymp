a = input()
counter = 0
while(int(a)>0):
	a = str(int(a)-sum(list(map(int, str(a)))))
	counter +=1
print(counter)