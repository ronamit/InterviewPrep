# ---------------------------------------------------------------------------------------------------------------------------#
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
# ---------------------------------------------------------------------------------------------------------------------------#
from collections import OrderedDict

class FreqStack:

    def __init__(self):
        self.stk = []
        self.num2count = dict() # key: item, val: count
        self.count2nums = dict() # key: count, val: set of items with that count in the stack
        self.most_freq_num = None
        self.most_freq_count = 0
        self.count2smaller_cnt = dict()  # key: count of some x in stack, val: the highest count of some x in stack that is smaller than key
    # end def

    def update_state(self, x, delta):
        '''
        updates counters and dicts
        '''
        if x in self.num2count: # if x equals to one of the elements in the stack
            old_cnt = self.num2count[x]
            self.count2nums[old_cnt].remove(x) # x is going to change its count
        else:
            old_cnt = 0
        # end if

        # update num2count:
        new_cnt = old_cnt + delta
        self.num2count[x] = new_cnt
        # clean-up memory:
        if new_cnt == 0: # x is no longer in the stack now
            del self.num2count[x]  # clean-up memory

        # update count2nums:
        if new_cnt not in self.count2nums:
            self.count2nums[new_cnt] = set()
        self.count2nums[new_cnt].add(x)
        # clean-up memory:
        if old_cnt in self.count2nums and len(self.count2nums[old_cnt]) == 0:
            del self.count2nums[old_cnt]

        # update most freq:
        self.count2nums[new_cnt].add(x)
        if new_cnt > self.most_freq_count:
            self.count2smaller_cnt[new_cnt] = self.most_freq_count
            self.most_freq_count = new_cnt
        # end if
        if new_cnt == self.most_freq_count:
            self.most_freq_num = x  # if equal we want the more recent element
        # end if

    # end def

    def push(self, x: int) -> None:
        # add to stack
        self.stk.append(x)
        # updates:
        self.update_state(x, delta=+1)
    # end def

    def pop(self) -> int:
        # remove from stack:
        x = self.stk.pop()
        # updates:
        self.update_state(x, delta=-1)
        return x
    # end def


# ---------------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------------#
ops_list = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
item_list = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output: [null, null, null, null, null, null, null, 5, 7, 5, 4]

stk = None
out_list = []
for i in range(len(ops_list)):
    op = ops_list[i]
    if op == "FreqStack":
        stk = FreqStack()
        out_list.append(None)
    elif op == "push":
        stk.push(item_list[i][0])
        out_list.append(None)
    elif op == "pop":
        out = stk.pop()
        out_list.append(out)
    # end if
# end for
# ---------------------------------------------------------------------------------------------------------------------------#
print(out_list)
print('count2nums: ', stk.count2nums)
print('most_freq_num: ', stk.most_freq_num)
print('most_freq_count: ', stk.most_freq_count)
print('count2smaller_cnt: ', stk.count2smaller_cnt)
# ---------------------------------------------------------------------------------------------------------------------------#