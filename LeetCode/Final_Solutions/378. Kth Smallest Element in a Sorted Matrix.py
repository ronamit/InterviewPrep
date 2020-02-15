

def kthSmallest(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    n = len(matrix)
    # Note: Trivial solution: Sort all of the elements is O(n^2log(n^2))
    # My solution  we only sort  possible candidates.
    # By simple logic, [count how many definitely larger and how many definitely smaller]
    # for index (i,j) the order k of this element is: (i+1)*(j+1) <= k <= n^2 - (n-i)*(m-j)+1
    list_cand = []
    n_smaller = 0
    n_larger = 0
    for i in range(n):
        j_start = (k-n*i-1) // (n-i)
        j_end = (k-1-i - 1)//(1+i) + 1
        if j_start > j_end:
            continue
        # j_start, j_end = min(j_start, j_end), max(j_start, j_end)
        j_end = min(j_end, n - 1)
        j_start = max(j_start, 0)
        n_smaller += j_start
        n_larger += n - j_end
        for j in range(j_start, j_end+1):
            list_cand += [matrix[i][j]]

    print(n_smaller)
    print(n_larger)
    print(list_cand)
    list_cand = sorted(list_cand)
    print(list_cand)
    return list_cand[(k - 1) - n_smaller]


# -------------------------------------------------------------
self = None
matrix = [
             [1, 5, 9, 41],
             [10, 11, 13, 45],
             [12, 13, 15, 46],
             [32, 43, 55, 66]
         ]
k = 8
# #
#
# matrix = [[-5]]
# k = 1

# matrix =  [[1,2],[3,3]]
# k = 3

print(kthSmallest(self, matrix, k))

#
# def FindKSmallest(s_r, e_r, s_c, e_c, kk):
#     n_rows = e_r - s_r + 1
#     n_cols = e_c - s_c + 1
#     if n_rows <= 2 and n_cols <= 2:
#         elements = [matrix[i][j] for i in range(s_r, e_r + 1) for j in range(s_c, e_c + 1)]
#         elements = sorted(elements)
#         return elements[kk - 1]
#     r_plus = max(kk // n_rows - 1, 0)
#     c_plus = max(kk // n_cols - 1, 0)
#     r_minus = max(n_rows - kk // n_rows + 1, 0)
#     c_minus = max(n_cols - kk // n_cols + 1, 0)
#     kk -= (r_plus) * n_rows + (c_plus) * n_cols
#     return FindKSmallest(s_r + r_plus, e_r - r_minus, s_c + c_plus, e_c - c_minus, kk)
#
#
# return FindKSmallest(0, n - 1, 0, n - 1, k)