def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':

    x = numerator
    if x==0: return '0'
    s = ''
    putMinus = (x > 0) != (denominator > 0)
    x = abs(x)
    denominator = abs(denominator)
    intPart = x // denominator
    x = x - intPart * denominator
    s = str(intPart)
    past = {x: len(s)}
    if x != 0:
        s += '.'
    ind = len(s)
    while (x != 0):
        x *= 10
        intPart = x // denominator
        x = x - intPart * denominator
        s += str(intPart)
        if x in past:
            repStart = past[x] + 1
            s = s[:repStart] + '(' + s[repStart:] + ')'
            break
        past[x] = ind
        ind += len(str(intPart))
    if putMinus:
        s = '-' + s
    return s



self = None
numerator = 1
denominator = 3
print(fractionToDecimal(self, numerator,denominator))

#
# def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':
#     intPart = numerator // denominator
#     rem = numerator - intPart * denominator
#     if rem == 0:
#         return str(intPart)
#     else:
#         outS = str(intPart) + "."
#     past = {}
#     ind = 2
#     x = rem
#     while (x != 0):
#         x = x * 10
#         intPart = x // denominator
#         outS += str(intPart)
#         x = x - intPart * denominator
#         if x in past:
#             repStart = past[x] + 1
#             outS = outS[:repStart] + '(' + outS[repStart:] + ')'
#             break
#         past[x] = ind
#         ind += 1
#     return outS
#
#
