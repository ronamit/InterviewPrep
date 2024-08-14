from collections import deque


class Solution:
    # TODO: use bin search to find min dist, then find the first it occurs with bin search, then find the k closest
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:

        n = len(arr)
        lo = 0
        hi = n - 1
        i_closest = None
        while lo < hi:
            mid = lo + (hi - lo) // 2
            d1 = abs(x - arr[mid - 1]) if mid > 0 else float("inf")
            d2 = abs(x - arr[mid])
            d3 = abs(x - arr[mid + 1]) if mid < n - 1 else float("inf")
            if d2 < min(d1, d3):
                i_closest = mid
                break
            if d1 > d2:
                lo = mid + 1
            else:
                hi = mid - 1
        i_closest = i_closest or lo
        ans = deque([arr[i_closest]])
        i = i_closest - 1
        j = i_closest + 1
        while len(ans) < k and i >= 0 and j < n:
            if abs(arr[i] - x) <= abs(arr[j] - x):
                ans.appendleft(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1
        while len(ans) < k and i >= 0:
            ans.appendleft(arr[i])
            i -= 1
        while len(ans) < k and j < n:
            ans.append(arr[j])
            j += 1
        return list(ans)


if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,4,4,4,4,5,5]
    k = 3
    x = 3
    print(sol.findClosestElements(arr, k, x))
