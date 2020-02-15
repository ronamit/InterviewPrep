class TreeNode:
    ''' Print is based on:
    https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python'''
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

    def insert(self, key, val):
        ''' Insertion under binary search tree rules'''
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = TreeNode(key, val)
            else:
                self.right.insert(key, val)
        else: # self.key > key
            if self.left is None:
                self.left = TreeNode(key, val)
            else:
                self.left.insert(key, val)


    def display(self, showVal = False):
        lines, _, _, _ = self._display_aux(showVal)
        for line in lines:
            print(line)

    def _display_aux(self, showVal):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if showVal:
            show = self.val
        else:
            show = self.key
        if self.right is None and self.left is None:
            line = '%s' % show
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux(showVal)
            s = '%s' % show
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux(showVal)
            s = '%s' % show
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux(showVal)
        right, m, q, y = self.right._display_aux(showVal)
        s = '%s' % show
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def build_tree(arr):
    '''' builds tree for an array representation '''
    n = len(arr)
    ptrs = [None for _ in range(n)]
    if n == 0: return None
    if n % 2 == 0:  arr += [None]
    for i in range(n//2):
        if arr[i] is not None:
            if ptrs[i] is None:
                ptrs[i] = TreeNode(arr[i])
            i_right = (i+1)*2
            if arr[i_right] is not None:
                ptrs[i_right] = TreeNode(arr[i_right])
                ptrs[i].right = ptrs[i_right]
            i_left = (i+1)*2 - 1
            if arr[i_left] is not None:
                ptrs[i_left] = TreeNode(arr[i_left])
                ptrs[i].left = ptrs[i_left]
    return ptrs[0]

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def SearchVal(root, v):
    if not root:
        return None
    if root.val == v:
        return root
    else:
        r_out = SearchVal(root.right, v)
        l_out = SearchVal(root.left, v)
        # if at least one of the children finds v
        if r_out:
            return r_out
        elif l_out:
            return l_out
        else:
            return None


if __name__ == "__main__":
    import random

    # b = TreeNode(50)
    # for _ in range(50):
    #     b.insert(random.randint(0, 100))

    # b = build_tree([3, 9, 20, None, None, 15, 7])
    b = build_tree([0, -3, 9, -10, None, 5])
    b.display()
    print('-'*50)
    stringToTreeNode("[1, null, 3, 2]").display()