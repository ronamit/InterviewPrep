import numpy as np

from typing import List

def check_word_fit(word: str, s: str):
    for i, c in enumerate(word):
        if c == s[i] or s[i] == " ":
            continue
        else:
            return False
    return True
        

def scan_vec(vec: list[str], word: str):
    # get all the sequnces between "#"
    seqs = "".join(vec).split("#")
    # remove empty strs
    seqs = [s for s in seqs if s]
    # keep only seqs with length ==  len(word)
    seqs = [s for s in seqs if len(s) == len(word)]

    # check if any seqs matches the word in non-white-space chars
    for s in seqs:
        if check_word_fit(word, s):
            return True
        # check reverse dir:
        if check_word_fit(word[::-1], s):
            return True            
    return False


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        board = np.array(board)
        m, n = board.shape
        # scan rows:
        for i in range(m):
            if scan_vec(board[i], word):
                return True
        # scan cols:
        for j in range(n):
            if scan_vec(board[:, j], word):
                return True
        return False



if __name__ == "__main__":
    board =[["#"," ","#"],[" "," ","#"],["#"," ","c"]]
    word = "ca"
    sol = Solution()
    print(sol.placeWordInCrossword(board, word))
    
