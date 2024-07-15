from typing import List


class Solution:
    def find_unconstrained_possible_seq(self, w: int):
        if w == 0:
            return [[]]
        configs = []
        for b in self.bricks:
            if b <= w:
                rest_of_seq = self.find_unconstrained_possible_seq(w - b)
                configs += [[b] + r for r in rest_of_seq]
        return configs

    def find_constrained_possible_seq(self, w: int, not_allowed_inds: list[set], start_idx=0):
        if w == 0:
            return [[]]
        configs = []
        for b in self.bricks:
            if (start_idx + b) in not_allowed_inds:
                continue  # position not allowed
            if b <= w:
                rest_of_seq = self.find_constrained_possible_seq(w - b, not_allowed_inds, start_idx=start_idx + b)
                configs += [[b] + r for r in rest_of_seq]
        return configs

    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        self.bricks = bricks

        # get all possible configs for first row
        all_possible_seq = self.find_unconstrained_possible_seq(width)

        # convert to tuples for hashing
        all_possible_seq = [tuple(seq) for seq in all_possible_seq]

        # remove duplicates
        all_possible_seq = list(set(all_possible_seq))
        print(f"Possible first row configurations: {all_possible_seq}")

        # enumerate all possible configs (unconstrained)
        all_possible_seq = [tuple(seq) for seq in all_possible_seq]
        n_possible_seq = len(all_possible_seq)
        seq_to_idx = {conf: i for i, conf in enumerate(all_possible_seq)}

        allowed_next_seq_per_seq = []  # for each possible sequence, find the possible allowed next/prev sequence

        for i_seq, seq in enumerate(all_possible_seq):
            separators = [0]
            print(f"Checking row config #{i_seq}: {seq}")
            # get the cumulative sum of bricks length to get the bricks separator locations
            for b in seq:
                separators.append(separators[-1] + b)
            # remove the first (0) and last (w - 1) locations
            separators = set(separators[1:-1])
            all_allowed_seq = self.find_constrained_possible_seq(width, separators)
            all_allowed_seq = [tuple(seq) for seq in all_allowed_seq]
            print(f"Allowed sequence in next row : {all_allowed_seq}")
            # convert to indexes:
            allowed_seq_inds = [seq_to_idx[seq] for seq in all_allowed_seq]
            print(f"Allowed sequence index in next row : {allowed_seq_inds}")
            allowed_next_seq_per_seq.append(allowed_seq_inds)

        print(f"Allowed next/prev row sequence indexes per conf: {allowed_next_seq_per_seq}")

        # Do dynamic programming to count the total number of possible.
        # F(i, j) = number of ways to build wall up to row i s.t. row i has seq j
        # F(1, any) = 1 (for all valid configs of the unconstrained row)
        # F(i, j) = sum over all  prev-rows seq k for. allowed for next=i, of F(i-1,k)

        max_num = (int)(1e9 + 7)
        F = [1 for _ in range(n_possible_seq)]
        F_prev = [1 for _ in range(n_possible_seq)]
        for h in range(1, height):
            for i in range(n_possible_seq):
                F[i] = 0
                for k in allowed_next_seq_per_seq[i]:
                    F[i] += F_prev[k] % max_num
            F_prev = F.copy()
        # The final answer sum_j F(height, j)
        ans = 0
        for i in range(n_possible_seq):
            ans += F[i] % max_num
        return ans


sol = Solution()
print(sol.buildWall(3, 5, [1, 2, 3]))
