from copy import deepcopy
from heapq import heapify, heappop


class Solution:
    def can_reach_end(self, final: int, heights: list[int], bricks: int, ladders: int) -> int:
        # the mininmal diffs should be covered by bricks
        diffs_min_heap = []
        for i in range(1, (final + 1)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                diffs_min_heap.append((diff, i))
        heapify(diffs_min_heap)
        inds_for_bricks = set()
        while diffs_min_heap:
            diff, i = heappop(diffs_min_heap)
            if bricks >= diff:
                bricks -= diff
                inds_for_bricks.add(i)
            else:
                break
        # print("inds_for_bricks", inds_for_bricks)
        for i in range(1, (final + 1)):
            # print(f"{i-1} to {i}")
            diff = heights[i] - heights[i - 1]
            if diff <= 0 or i in inds_for_bricks:
                continue
                # print("brick")
            if ladders > 0:
                # print("ladder")
                ladders -= 1
            else:
                return False
        return True

    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_reach = 0
        while left <= right:
            mid = left + (right - left) // 2
            if self.can_reach_end(final=mid, heights=heights, bricks=deepcopy(bricks), ladders=deepcopy(ladders)):
                max_reach = max(max_reach, mid)
                left = mid + 1
                # print("Can reach ", mid)
            else:
                # print("Can't reach ", mid)
                right = mid - 1
        return max_reach
