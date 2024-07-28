class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowels_inds = []
        for i, c in enumerate(s):
            if c in vowels:
                vowels_inds.append(i)

        new_s = ""
        i_vowel = 0
        for c in s:
            if c not in vowels:
                new_s += c
            else:
                new_s += s[vowels_inds[-i_vowel - 1]]
                i_vowel += 1
        return new_s
