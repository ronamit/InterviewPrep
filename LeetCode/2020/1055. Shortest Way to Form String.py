class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        i = 0
        n_subs = 0
        while i < len(target):
            n_subs += 1
            is_update = False
            for j, s in enumerate(source):
                if i == len(target):
                    break
                if s == target[i]:
                    i += 1
                    is_update = True
            if not is_update:
                break
        if i == len(target):
            return n_subs
        else:
            return -1
