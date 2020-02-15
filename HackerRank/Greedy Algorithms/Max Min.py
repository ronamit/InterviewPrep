
# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    n = len(arr)
    min_dist =  arr[k-1] - arr[0]
    for i in range(k, n):
        dist = arr[i] - arr[i-k+1]
        min_dist = min(min_dist, dist)
    return min_dist

k = 3
arr = [1,2,3,4,10,20,30,40,100,200]
print(maxMin(k, arr))