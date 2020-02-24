class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # longest valid == (i-height of stack during run)
        stk = []
        max_val = -1
        for i, c in enumerate(s):
            if c == '(':
                stk.append(c)
            elif c == ')':
                if stk:
                    stk.pop()
            max_val = max(max_val, i - len(stk))
        return max_val


sol = Solution()
print(sol.longestValidParentheses(")()())"))