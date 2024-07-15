
from typing import List

class Solution:

    def find_one_row_configs(self, w: int):
        if w == 0:
            return [[]]
        configs = []
        for b in self.bricks:
            if b <= w:
                rest_configs = self.find_one_row_configs(w - b)
                configs += [[b] + r for r in rest_configs]
        return configs

    def find_one_row_configs_constrained(
        self, w: int, prev_separators: list[set], start_idx=0
    ):
        if w == 0:
            return [[]]
        configs = []
        for b in self.bricks:
            if (start_idx + b) in prev_separators:
                continue  # position not allowed
            if b <= w:
                rest_configs = self.find_one_row_configs_constrained(
                    w - b, prev_separators, start_idx=start_idx + b
                )
                configs += [[b] + r for r in rest_configs]
        return configs

    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        self.bricks = bricks

        # get all possible configs for first row
        all_confs = self.find_one_row_configs(width)
        
        # enumerate all possible configs (unconstraiend)
        all_confs = [tuple(conf) for conf in all_confs]
        n_confs = len(all_confs)
        conf_to_idx = {conf: i for i, conf in enumerate(all_confs)}

        allowed_adj_row_per_conf = [] # for each possible config, find the allowed next/prev row config

        for conf in all_confs:
            separators = [0]
            # get the cumulative sum of bricks length to get the bricks separator locations
            for b in conf:
                separators.append(separators[-1] + b)
            # remove the first (0) and last (w - 1) locations
            separators = set(separators[1:-1])
            allowed_configs = self.find_one_row_configs_constrained(width, separators)
            
            # convert to indexes:
            allowed_configs = [conf_to_idx[tuple(conf)] for conf in allowed_configs]
            
            allowed_adj_row_per_conf.append(allowed_configs)

        # Do dynamic programming to count the total number of possible.
        # F(i, j) = number of ways to build wall up to row i s.t. row i has seq j
        # F(1, any) = 1 (for all valid configs of the unconstrained row)
        # F(i, j) = sum over all  prev-rows seq k for. allowed for next=i, of F(i-1,k)

        max_num = (int)(1e9 + 7)
        F = [1 for _ in range(n_confs)]
        F_prev = [1 for _ in range(n_confs)]
        for h in range(1, height):
            for i in range(n_confs):
                F[i] = 0
                for k in allowed_adj_row_per_conf[i]:
                    F[i] += F_prev[k] % max_num
            F_prev = F
        # The final answer sum_j F(height, j)
        ans = 0
        for i in range(n_confs):
            ans += F[i] % max_num
        return ans



sol = Solution()
print(sol.buildWall(3, 5, [1, 2, 3]))