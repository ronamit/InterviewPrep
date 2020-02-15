def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> 'int':
    sumsCounts = {}
    def addToDict(d, k, v):
        if k not in d:
            d[k] = v
        else:
            d[k] += v
    for i in range(len(A)):
        for j in range(len(B)):
            s = A[i] + B[j]
            addToDict(sumsCounts, s, 1)
    # to save memory:
    sumsCounts = list(zip(sumsCounts.keys(), sumsCounts.values()))
    sumsCounts2 = {}
    while sumsCounts:
        s1, cnt1 = sumsCounts.pop()
        for i in range(len(C)):
            s2 = s1 + C[i]
            addToDict(sumsCounts2, s2, cnt1)

    sumsCounts2 = list(zip(sumsCounts2.keys(), sumsCounts2.values()))

    count = 0
    while sumsCounts2:
        s2, cnt2 = sumsCounts2.pop()
        for i in range(len(D)):
                s3 = s2 + D[i]
                if s3 == 0:
                    count += cnt2
    return count


self = None
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(fourSumCount(self, A, B, C, D))

#
# def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> 'int':
#     count = 0
#     for i in range(len(A)):
#         for j in range(len(B)):
#             for k in range(len(C)):
#                 for l in range(len(D)):
#                     count += (A[i] + B[j] + C[k] + D[l] == 0)
#     return count

#

sumsCounts = {}


def addToDict(d, k, v):
    if k not in d:
        d[k] = v
    else:
        d[k] += v
#
#
# for i in range(len(A)):
#     for j in range(len(B)):
#         s = A[i] + B[j]
#         addToDict(sumsCounts, s, 1)
# negS2 = {}
# posS2 = {}
# zeroS2Count = 0
# for i in range(len(C)):
#     for s1 in sumsCounts.keys():
#         s2 = s1 + C[i]
#         cnt1 = sumsCounts[s1]
#         if s2 < 0:
#             addToDict(negS2, s2, cnt1)
#         elif s2 > 0:
#             addToDict(posS2, s2, cnt1)
#         else:
#             zeroS2Count += cnt1
# del sumsCounts
# negD = list(filter(lambda x: x < 0, D))
# posD = list(filter(lambda x: x > 0, D))
# zeroD = list(filter(lambda x: x == 0, D))
# count = 0
# for i in range(len(negD)):
#     for s3 in posS2:
#         if negD[i] + s3 == 0:
#             count += posS2[s3]
# for i in range(len(posD)):
#     for s3 in negS2:
#         if posD[i] + s3 == 0:
#             count += negS2[s3]
# count += len(zeroD) * zeroS2Count
# return count