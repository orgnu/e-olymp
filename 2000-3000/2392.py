def kicik(a):
    rqmlr = [i for i in a]
    rqmlr = sorted(rqmlr)
    if rqmlr[0] == '0':
        rqmlr[0], rqmlr[1] = rqmlr[1], rqmlr[0]
    if rqmlr[0] == '0':          
        rqmlr[0], rqmlr[2] = rqmlr[2], rqmlr[0]
    return int(''.join(rqmlr))

def boyuk(a):
    rqmlr = [i for i in a]
    rqmlr = list(reversed(sorted(rqmlr)))
    return int(''.join(rqmlr))


a = input()
print(kicik(a) + boyuk(a))