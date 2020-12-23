# ---------------------------------------------------------------------------------------------------------------------------#
# https://leetcode.com/problems/maximum-frequency-stack/
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

# TODO: there is a flaw in this - if we poped some value we add it to the count2nums of the val-1, but we lose the insertion order to the stack
# TODO: On second tought, mybe it is not a problem... but we may need that the lement of count2nums to be stacks tp keep insertion order
# ---------------------------------------------------------------------------------------------------------------------------#
from OrderedSet import OrderedSet
from DoublyLinkedListUnique import DoublyLinkedListUnique


class FreqStack:

    def __init__(self):
        self.num2count = dict()  # key: num, val: count of num in stack
        self.count2nums = dict()  # key: count, val: set of nums with that count in the stack
        self.pop_candidate = None  # The num to pop first
        self.pop_candidate_count = 0  # pop_candidate's count
        self.counts_list = DoublyLinkedListUnique()  # ordered list of all the counts of elements in the stack
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
            self.count2nums[old_cnt].discard(x)  # because x is going to change its count
            if len(self.count2nums[old_cnt]) == 0:
                # If old_cnt is no longer exist in the list, we need to update some stuff
                del self.count2nums[old_cnt]  # clean-up memory
                # Check if we need to update the candidate for pop:
                if old_cnt == self.pop_candidate_count:
                    self.pop_candidate_count = self.counts_list.get_val_prev_to_val(old_cnt)
                    # take the last inserted num with this count
                    self.pop_candidate = self.count2nums[self.pop_candidate_count].last()
                self.counts_list.delete_val(old_cnt)
        else:
            old_cnt = 0
        # end if

        new_cnt = old_cnt + delta
        if new_cnt > 0: # if it is, we don't save it in the state
            self.num2count[x] = new_cnt

        # update count2nums:
        if new_cnt not in self.count2nums:
            self.count2nums[new_cnt] = OrderedSet([x])
        else:
            self.count2nums[new_cnt].add(x)
            # TODO: this is problematic, since now x is the last element in count2nums[new_cnt], even if it is not the last inserted
        # end if

        if delta > 0:
            self.counts_list.insert_after_value(old_cnt, new_cnt)
        else:
            self.counts_list.insert_before_value(old_cnt, new_cnt)

        # If the inserted item need to be set as the 'pop candidate':
        if new_cnt >= self.pop_candidate_count:  # includes the equal case since we want the more recent element
            self.pop_candidate = x
            self.pop_candidate_count = new_cnt
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
    print('pop_candidate: ', stk.pop_candidate)
    print('pop_candidate_count: ', stk.pop_candidate_count)
    print('counts_list: ', stk.counts_list)
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