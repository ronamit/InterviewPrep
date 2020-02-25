# User function Template for python3
''' Your task is to returns 1 if there is triplet with sum equal
    to 0 present in A[], else return 0'''


def findTriplets(a, n):
    # code here

    # Split to positives and negatives

    # for each negative - see if there are two positives that sums to its absolute value
    # O(|negatives|*|positives|)

    positives = [i for i in range(n) if a[i] >= 0]
    negatives = [i for i in range(n) if a[i] < 0]

    # pos_set = Set([x for x in a if x >= 0])
    # neg_set = Set([x for x in a if x < 0])

    # Check option for three zeros
    if a.count(0) >=3:
        return 1

    # Check option for one negative and two positives
    for i in negatives:
        target = -a[i]
        seen = set([])
        for j in positives:
            if (target - a[j]) in seen:
                return 1
            seen.add(a[j])

    # Check option for one positive and two negatives
    for i in positives:
        target = -a[i]
        seen = set([])
        for j in negatives:
            if (target - a[j]) in seen:
                return 1
            seen.add(a[j])

    return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(findTriplets(a, n))
# } Driver Code Ends