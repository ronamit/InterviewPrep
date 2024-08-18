class Solution:
    def findReplaceString(
        self,
        s: str,
        indices: list[int],
        sources: list[str],
        targets: list[str],
    ) -> str:
        replaces = []  # list of (start_idx_in_orig, end_idx_in_orig, new_s)
        # of the position to delete in orig and the string to put instead
        k = len(indices)
        for i in range(k):
            ind = indices[i]
            src = sources[i]
            if s[ind : (ind + len(src))] == src:
                replaces.append((ind, ind + len(src), targets[i]))
        if len(replaces) == 0:
            return s
        # sort by start index
        replaces.sort()
        new_s = s[: replaces[0][0]]
        for i, r in enumerate(replaces):
            # add the target
            new_s += r[2]
            # add the chars from original before next replace:
            if i < len(replaces) - 1:
                next_replace_start = replaces[i + 1][0]
                new_s += s[r[1] : next_replace_start]
        # add the rest (the part of the original s after all the replaces)
        last_rep_end = replaces[-1][1]
        if last_rep_end < len(s):
            new_s += s[last_rep_end:]
        return new_s
        # O(k log(k) + sum of string lengths)
