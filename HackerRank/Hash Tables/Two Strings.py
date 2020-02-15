def twoStrings(s1, s2):
    d = {}
    for c in s1:
        if c not in d:
            d[c] = 0
        d[c] += 1
    for c in s2:
        if c in d:
            return ('YES')
    return ('NO')

s1 = 'ads'
s2 = 'bs'
print(twoStrings(s1, s2))
