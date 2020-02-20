
import string

def count(s):
    n_let = len(string.ascii_lowercase)
    hist = [0] * n_let
    for c in s:
        ind = ord(c) - ord('a')
        hist[ind] += 1
    return tuple(hist)

def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anag_dict = {}
    for i, s in enumerate(strs):
        char_count = count(s)
        if char_count in anag_dict:
            anag_dict[char_count] += [i]
        else:
            anag_dict[char_count] = [i]

    anag_list = []
    for str_inds in anag_dict.values():
        anag_list.append([strs[i] for i in str_inds])
    return anag_list

self = None
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(self, strs))