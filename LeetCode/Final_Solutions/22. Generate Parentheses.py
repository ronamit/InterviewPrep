
def generateParenthesisR(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    # get the solution for n-1:
    prev = generateParenthesisR(n-1)
    out = []
    for s in prev:
        # add the opening bracket
        s_new = '(' + s
        slen = len(s_new)
        op = 0
        cl = 0
        # find valid inds for a closing bracket
        #  - when the '(' counter equals the ')' counter
        for i in range(1, slen+1):
            if op == cl:
                out += [s_new[:i] + ')' + s_new[i:]]
            if i < slen:
                op += (s_new[i] == '(')
                cl += (s_new[i] == ')')
    return out


def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    return generateParenthesisR(n)

self = None
n = 3
print(generateParenthesis(self, n))
