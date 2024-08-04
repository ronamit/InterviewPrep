import string

alphabet = string.ascii_lowercase


class WordDictionary:

    def __init__(self):
        self.mem = set()

    def addWord(self, word: str) -> None:
        self.mem.add(word)

    def search(self, word: str) -> bool:
        first_dot_idx = word.find(".")
        if first_dot_idx == -1:
            return word in self.mem
        return any(self.search(word[:first_dot_idx] + c + word[first_dot_idx + 1 :]) for c in alphabet)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
