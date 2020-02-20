
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    brk_stck = []
    for a in s:
        if a in ['(', '[', '{']:
            brk_stck.append(a)
        else:
            if not brk_stck:
                return False
            p = brk_stck.pop()
            if not (p,a) in [('(', ')'), ('[', ']'), ('{', '}')]:
                return False
    return brk_stck == []


s = "{[]}"
self = None
print(isValid(self, s))