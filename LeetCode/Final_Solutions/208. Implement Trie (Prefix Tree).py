import string


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        n_symbols = len(string.ascii_letters) + 1
        self.childs = [None for _ in range(n_symbols)]

    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        n = len(word)
        p = self
        for i in range(n):
            c = word[i]
            c_ind = ord(c) - ord('a')
            if p.childs[c_ind] is None:
                p.childs[c_ind] = Trie()
            p = p.childs[c_ind]

        p.childs[-1] = Trie()  # end of string

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        n = len(word)
        p = self
        for i in range(n):
            c = word[i]
            c_ind = ord(c) - ord('a')
            if p.childs[c_ind] is None:
                return False
            else:
                p = p.childs[c_ind]
                # return True if there is an end of string symbol at end of scan:
        return not (p.childs[-1] is None)

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = len(prefix)
        p = self
        for i in range(n):
            c = prefix[i]
            c_ind = ord(c) - ord('a')
            if p.childs[c_ind] is None:
                return False
            else:
                p = p.childs[c_ind]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)