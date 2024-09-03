class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        i_pop = 0
        for x_push in pushed:
            stack.append(x_push)
            while stack and popped[i_pop] == stack[-1]:
                stack.pop()
                i_pop += 1
        return i_pop == len(popped)
