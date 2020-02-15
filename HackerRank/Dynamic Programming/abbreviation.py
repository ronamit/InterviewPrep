
# def abbreviation(a, b):
#     if abbreviation_aux(a, b):
#         return 'YES'
#     else:
#         return 'NO'
#
# def abbreviation_aux(a, b):
#     # print((a,b))
#     if a == b:
#         return True
#     if len(b) == 0:
#         return a.islower()
#     if len(a) < len(b):
#         return False
#     # one option: keep the first letter of a, then it must match the first letter of B
#     if a[0].upper() == b[0] and abbreviation_aux(a[1:], b[1:]):
#         return True
#     # second option: if a[0] is lower we can drop it
#     if a[0].islower() and abbreviation_aux(a[1:], b):
#         return True
#     return False


# def abbreviation(a, b):
#     if abbreviation_aux(a, b):
#         return 'YES'
#     else:
#         return 'NO'

def abbreviation(a, b):
    na = len(a)
    nb = len(b)
    #  we want to calculate the matrix V[i,j]
    # V[i,j] == can a[:i] be converted to b[:j], i=0..,na, j=0,..,nb
    # to calculate V[i,j] we need V[i-1,j] and V[i-1,j-1]
    # we calculate on row at a time to save memory
    # Init first row:: V[0,:], i.e, a=="", in this case b[:j] can only be converted if it is empty
    row = [False for _ in range(nb+1)]
    row[0] = True # if a==b==""
    for i in range(1, na+1):
        prev_row = row.copy()
        for j in range(nb+1):
            row[j] = (a[i-1].islower() and prev_row[j]) \
                      or (j > 0 and a[i-1].upper() == b[j-1] and prev_row[j-1])
    # finally, check if a[:na+1] can be converted to b[:nb+1]
    if row[-1]:
        return 'YES'
    else:
        return 'NO'

a = 'daB'
b = 'ABC'
print(abbreviation(a, b))