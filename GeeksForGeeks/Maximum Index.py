# code
# https://practice.geeksforgeeks.org/problems/maximum-index/0
# https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

def BinSearch_FirstSmaller(L, x):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (high + low) // 2
        if L[mid][1] <= x:
            if (mid == 0 or L[mid - 1][1] > x):
                # first smaller
                return L[mid][0]
            else:
                # smaller, but not first - go left
                high = mid - 1
            # end if
        else:
            # go right
            low = mid + 1
        # end if
        # end while
        return -1  # not found


# end def

def MaximumIndex(a):
    n = len(a)
    L = []
    cur_min = -float('inf')
    max_dist = -1  # default == not found
    for j in range(n):
        if a[j] < cur_min:
            L.append((j, a[j]))
        # end if
        i = BinSearch_FirstSmaller(L, a[j])
        if i != -1:
            max_dist = max(max_dist, j - i)
        # end if
    # end for
    return max_dist


# end def


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        a = [int(x) for x in input().strip().split()]
        # --------------------------------------------------------------
        print(MaximumIndex(a))
        # --------------------------------------------------------------
        t = t - 1

