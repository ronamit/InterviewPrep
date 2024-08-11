class Solution:
    def decodeString(self, s: str) -> str:
        print(s)
        # Find if the string starts with alphabet substring:
        prefix_s = ""
        i = 0
        while i < len(s) and s[i].isalpha():
            prefix_s += s[i]
            i += 1
        if i == len(s):
            return prefix_s
        # check if there is a number after prefix_s
        prefix_num = 0
        while s[i].isdigit() and i < len(s):
            prefix_num = prefix_num * 10 + int(s[i])
            i += 1
        # Now, there must be brackets, we need to call the function recousively. and then continue with rest of string recusively
        brk_start = i
        count = 1
        i += 1
        while count > 0 and i < len(s):
            if s[i] == "[":
                count += 1
            elif s[i] == "]":
                count -= 1
            i += 1
        brk_end = i
        decoded_sub = self.decodeString(s[(brk_start + 1) : (brk_end - 1)])
        if brk_end < len(s):
            decoded_rest = self.decodeString(s[brk_end:])
        else:
            decoded_rest = ""
        return prefix_s + prefix_num * decoded_sub + decoded_rest


if __name__ == "__main__":
    sol = Solution()
    s = "3[a]2[bc]"
    print(sol.decodeString(s))
