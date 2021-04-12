a, b, c = map(int, input().split())
kublar = a * b * c
tamuz = kublar * 6
lazimuz = 2 * (a * b + a * c + b * c)
cavab = tamuz - lazimuz
print (kublar, cavab)