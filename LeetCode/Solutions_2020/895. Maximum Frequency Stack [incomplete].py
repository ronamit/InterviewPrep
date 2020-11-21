# ---------------------------------------------------------------------------------------------------------------------------#
# https://leetcode.com/problems/maximum-frequency-stack/
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
# ---------------------------------------------------------------------------------------------------------------------------#
from OrderedSet import OrderedSet
from DoublyLinkedListUnique import DoublyLinkedListUnique



class FreqStack:

    def __init__(self):
        self.num2count = dict() # key: num, val: count of num in stack
        self.count2nums = dict() # key: count, val: set of nums with that count in the stack
        self.pop_candidate = None # The num to pop first
        self.pop_candidate_count = 0 # pop_candidate's count
        self.counts_list = DoublyLinkedListUnique()

        self.count2smaller_cnt = dict()  # key: count of some num in stack, val: the highest count of some x in stack that is smaller than num
        self.count2higher_cnt = dict()   # key: count of some num in stack, val: the highest count of some x in stack that is smaller than num
        # those two allow a 'doubly-linked-list' structure,
        # so it is O(1) easy to add\remove counts and go from one count to its two adajecnts ones.
        # end def


    def update_state(self, x, delta):
        '''
        Change the count of x by delta
        '''
        is_in_stack = x in self.num2count
        if not is_in_stack and delta == -1:
            raise ValueError('Can not remove!')

        if is_in_stack:
            old_cnt = self.num2count[x]
            self.count2nums[old_cnt].discard(x) # because x is going to change its count
            if len(self.count2nums[old_cnt]) == 0:
                del self.count2nums[old_cnt]   # clean-up memory
        else:
            old_cnt = 0
        # end if
        new_cnt = old_cnt + delta
        self.num2count[x] = new_cnt

        # update pop_candidate:
        if new_cnt >= self.pop_candidate_count:  # includes the equal case since we want the more recent element
            self.pop_candidate = x
            self.pop_candidate_count = new_cnt
        # end if
        if x == self.pop_candidate and new_cnt < self.pop_candidate_count:
            # in this case the count of x is lowered by 1,  so if it was the pop_candidate we may now not be
            if not (self.pop_candidate_count in self.count2nums and self.count2nums[self.pop_candidate_count] > 0):
             # in case there is no longer any num in the stack with the same count as pop_candidate_count
             self.pop_candidate_count = self.count2smaller_cnt[self.pop_candidate_count]
            # end if
            # get the last added item to the set (possible since it is an OrderedSet):
            self.pop_candidate = self.count2nums[self.pop_candidate_count].pop(last=True)
            self.count2nums[self.pop_candidate_count].add(self.pop_candidate)  # re-insert
        # end if

        # update count2nums:
        if new_cnt not in self.count2nums and new_cnt > 0:
            self.count2nums[new_cnt] = OrderedSet()
        # end if
        if new_cnt > 0:
            self.count2nums[new_cnt].add(x)
        # end if

        # update count2smaller_cnt:
        if new_cnt == 1:
            self.count2smaller_cnt[1] = 0
        elif old_cnt not in self.count2nums:
            self.count2smaller_cnt[new_cnt] = self.count2smaller_cnt[old_cnt]
            del self.count2smaller_cnt[old_cnt]
        # end if
    # end def

    def push(self, x: int) -> None:
        self.update_state(x, delta=+1)
    # end def

    def pop(self) -> int:
        # remove from stack:
        x = self.pop_candidate
        self.update_state(x, delta=-1)
        return x
    # end def
# end class

# ---------------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------------#
ops_list = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
item_list = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output: [null, null, null, null, null, null, null, 5, 7, 5, 4]

stk = None
out_list = []
for i in range(len(ops_list)):
    op = ops_list[i]
    print("-"*20, "Round ", i, ', ', op, ' - ', item_list[i], "-"*20)
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
    print('Output: ', out_list)
    print('num2count: ', stk.num2count)
    print('count2nums: ', stk.count2nums)
    print('most_freq_num: ', stk.pop_candidate)
    print('most_freq_count: ', stk.pop_candidate_count)
    print('count2smaller_cnt: ', stk.count2smaller_cnt)
    pass
# end for
print('Final output: ', out_list)
# ---------------------------------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------------------------------#

#
# self.count2smaller_cnt[new_cnt] = self.pop_candidate_count
#
# self.pop_candidate_count = new_cnt
# self.pop_candidate = x
#
# elif delta == -1 and (self.pop_candidate_count in self.count2nums) and (
#             len(self.count2nums[self.pop_candidate_count]) == 0):
# self.pop_candidate_count = self.count2smaller_cnt[self.pop_candidate_count]
# self.pop_candidate = self.count2nums[self.pop_candidate_count][-1]  # take the last added with this count
# # end if
# # end if