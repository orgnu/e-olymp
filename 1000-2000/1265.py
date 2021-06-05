def misir():
    (a, b, c) = map(int, input().split())
    if(a == 0 and b == 0 and c == 0):
        return 0
    elif((a**2 == b**2+c**2) or (b**2 == a**2+c**2) or (c**2 == b**2+a**2)):
        print('right')
        misir()
    else:
        print('wrong')
        misir()

misir()