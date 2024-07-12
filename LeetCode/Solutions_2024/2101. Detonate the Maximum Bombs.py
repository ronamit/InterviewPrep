from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # find the directed graph  O(n^2)
        n = len(bombs)
        adj_list = [[] for _ in range(n)]
        for i1 in range(n):
            for i2 in range(i1+1, n):
                bomb1 = bombs[i1]
                bomb2 = bombs[i2]
                dist_sqr = (bomb1[0] - bomb2[0])**2 + (bomb1[1] - bomb2[1])**2
                r1 = bomb1[2]
                r2 = bomb2[2]
                if r1 ** 2 >= dist_sqr:
                    adj_list[i1].append(i2)
                if r2 ** 2 >= dist_sqr:
                    adj_list[i2].append(i1)
        
        # loop over the nodes and run DFS from each 
        print(adj_list)

        def count_explodes(i: int, exploded_already: set) -> int:
            if i in exploded_already:
                return 0
            exploded_already.add(i)
            n_explodes = 1
            for c in adj_list[i]:
                n_explodes += count_explodes(c, exploded_already)
            return n_explodes
                    
        max_explodes = 0
        for i in range(n):
            exploded_already = set()
            max_explodes = max(max_explodes, count_explodes(i, exploded_already))
        return max_explodes


if __name__ == '__main__':
    bombs =[[2,1,3],[6,1,4]]
    sol = Solution()
    print(sol.maximumDetonation(bombs))