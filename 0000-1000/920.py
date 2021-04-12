x, y, z = map(float,(input().split()))
print(min(max(x,y), max(y,z), x+y+z))