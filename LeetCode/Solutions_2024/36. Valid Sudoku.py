class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for i0 in range(0, 9, 3):
            for j0 in range(0, 9, 3):
                seen = set()
                for di in range(3):
                    for dj in range(3):
                        i = i0 + di
                        j = j0 + dj
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])

        return True
