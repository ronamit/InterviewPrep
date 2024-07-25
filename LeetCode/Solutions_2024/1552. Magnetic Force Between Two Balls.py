import math


class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        n = len(position)
        # Sort:
        position.sort()
        print(position)

        # do a binary search to find the max  min-distance (since when some distance is valid min-distance then all higher are valid, and if it is invalid then all lower are invalid)

        def is_valid_min_dist(d: int) -> bool:
            # go over the (sorted) positions, put a ball in the first bin then in the next bin that is a at least at distance d and so on
            nonlocal position, m, n
            last_ball_pos = position[0]
            idx = 1  # scan index in the position array
            n_placed = 1
            # print(f"Placed #{n_placed} ball at {last_ball_pos}")
            while idx < n:
                if (position[idx] - last_ball_pos) >= d:
                    # place a ball here (we passed the min dist)
                    n_placed += 1
                    last_ball_pos = position[idx]
                    # print(f"Placed ball #{n_placed} at {last_ball_pos}")
                    if n_placed == m:
                        return True
                idx += 1
            # check if all balls placed successfully:
            return n_placed == m

        # use b
        # the boundaries of the search [1, ceil((p_max-p_min)/(m-1))]
        p_min = position[0]
        p_max = position[-1]
        left = 1
        right = math.ceil((p_max - p_min) / (m - 1))
        # right = (p_max - p_min)
        while left < right:
            mid = math.ceil((left + right) / 2)
            is_valid = is_valid_min_dist(mid)
            # print(f"{mid} is valid min distance? {is_valid}")
            if is_valid:
                # try longer distances
                left = mid
            else:
                # try shorter distances
                right = mid - 1
        return left


if __name__ == "__main__":
    position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = 4
    print(Solution().maxDistance(position, m))
