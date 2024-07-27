class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        num = 0
        while i < len(s) and s[i] == "M":
            num += 1000
            i += 1
        if s[i : i + 2] == "CM":
            num += 900
            i += 2
        while i < len(s) and s[i] == "D":
            num += 500
            i += 1
        if s[i : i + 2] == "CD":
            num += 400
            i += 2
        while i < len(s) and s[i] == "C":
            num += 100
            i += 1
        if s[i : i + 2] == "XC":
            num += 90
            i += 2
        while i < len(s) and s[i] == "L":
            num += 50
            i += 1
        if i < len(s) and s[i : i + 2] == "XL":
            num += 40
            i += 2
        while i < len(s) and s[i] == "X":
            num += 10
            i += 1
        if i < len(s) and s[i : i + 2] == "IX":
            num += 9
            i += 2
        while i < len(s) and s[i] == "V":
            num += 5
            i += 1
        if s[i : i + 2] == "IV":
            num += 4
            i += 2
        while i < len(s) and s[i] == "I":
            num += 1
            i += 1
        return num
