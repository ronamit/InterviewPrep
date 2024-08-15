class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        cur_change = {5: 0, 10: 0}
        for payed_bill in bills:
            if payed_bill == 5:
                cur_change[5] += 1
            elif payed_bill == 10:
                if cur_change[5] == 0:
                    return False
                cur_change[5] -= 1
                cur_change[10] += 1
            elif payed_bill == 20:
                if cur_change[10] >= 1 and cur_change[5] >= 1:
                    cur_change[10] -= 1
                    cur_change[5] -= 1
                    # no need to keep 20 bills
                elif cur_change[5] >= 3:
                    cur_change[5] -= 3
                else:
                    return False
        return True
