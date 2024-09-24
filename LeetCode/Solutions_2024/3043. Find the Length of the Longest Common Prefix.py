class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:

        # create a Trie to save all the numbers in arr1
        trie_root = {}
        for num in arr1:
            digits = str(num)
            node = trie_root
            for digit in digits:
                if digit not in node:
                    node[digit] = {}
                node = node[digit]
                node["#"] = {}  # end token

        max_prefix_len = 0
        for num in arr2:
            cur_prefix_len = 0
            digits = str(num)
            node = trie_root
            for digit in digits:
                if digit in node:
                    cur_prefix_len += 1
                    node = node[digit]
                else:
                    break
                max_prefix_len = max(max_prefix_len, cur_prefix_len)
        return max_prefix_len
