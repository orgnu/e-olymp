a = input()
b = list(a)
counter = 0
for i in b:
	if(i == '.' or i=='!' or i=='?'):
		counter +=1
print(counter)