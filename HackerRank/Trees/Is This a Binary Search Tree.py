""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
from TreeClass import  stringToTreeNode

# TODO: the sets are not needed...

def checkBST_lims(t, low, high):
    if t is None:
        return True, set()
    # print((low,high), t.data)
    if (low is not None and t.data <= low) or (high is not None and t.data >= high):
        print("Vale {} not in range ({},{})".format(t.data, low, high))
        return False, set()
    print("Vale {}  in range ({},{})".format(t.data, low, high))

    if low is not None:
        new_low = min(low, t.data)
    else:
        new_low = t.data
    if high is not None:
        new_high = max(high, t.data)
    else:
        new_high = t.data
    ans_left, seen = checkBST_lims(t.left, low, new_high)
    ans_right, seen_right = checkBST_lims(t.right, new_low, high)
    if seen.intersection(seen_right):
        return False, set()
    seen.union(seen_right)
    ans = (t.data not in seen) and ans_left and ans_right
    seen.add(t.data)
    return ans, seen

def checkBST(root):
    ans, seen = checkBST_lims(root, None, None)
    return ans

input = '1 2 3 4 5 6 7 8 9 10 11 13 12 14 15'
root = stringToTreeNode(input, separator=' ')
root.display()
print(checkBST(root))