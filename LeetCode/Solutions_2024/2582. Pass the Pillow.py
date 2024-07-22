class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # the movement is (2*n - 2)-periodic, so we can look only at  time % (2 * n - 2)
        t = time % (2 * n - 2)
        if t <= (n - 1):
            # only moves forward
            pos = 1 + t
        else:  #  n < t < 2*n
            # moves backward after the first n steps
            pos = 2 * n - t - 1
        return pos
