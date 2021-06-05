from math import sin
a, b, h = map(float, input().split(' '))
while a <= b:
    y = 3 * sin(a)
    print("%.3f %.3f" % (a, y))
    a += h