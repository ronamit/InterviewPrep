# Complete the countTriplets function below.
def countTriplets(arr, r):
    counts = dict()
    n_trip = 0
    n = len(arr)
    # the array pair_cnt will be the number of ordered pairs (x,r*x) which start at x = arr[i]
    pair_cnt = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x = arr[i]
        if x % r != 0:
            continue # we need to count only pairs that can be a triplet later
        # check if r*x has been seen in he rest of the array
        if r*x in counts:
            pair_cnt[i] = counts[r*x]
        # update counts for next iterations:
        if x not in counts:
            counts[x] = 0
        counts[x] += 1
    counts_pairs = {}
    # counts_pairs will say how many pairs (x,r*x) has been seen in the rest of the array after index i
    for i in range(n-1, -1, -1):
        x = arr[i]
        if r*x in counts_pairs:
            n_trip += counts_pairs[r*x]
        # update for next iterations:
        if x not in counts_pairs:
            counts_pairs[x] = 0
        counts_pairs[x] += pair_cnt[i]
    return n_trip



arr = [1,1,1]
r = 1
print(countTriplets(arr, r))