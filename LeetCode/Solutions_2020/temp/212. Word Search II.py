from typing import List, Dict, Tuple, Sequence
import itertools, collections
import string
from copy import deepcopy


class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		n = len(board)
		m = len(board[0])

		def neig(i, j):
			for (i2, j2) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
				if 0 <= i2 <= n - 1 and 0 <= j2 <= m - 1:
					yield (i2, j2, board[i2][j2])

		char_pos = {c: [] for c in string.ascii_lowercase}
		for i in range(n):
			for j in range(m):
				c = board[i][j]
				char_pos[c].append((i,j))
			# end for j
		# end for i

		words_found = []
		for word in words:
			c = word[0]
			pos = list(char_pos[c]) # paths' heads
			if not pos:
				continue
			paths = [{p} for p in pos] # save path to prevent using same position in a path
			for c in word[1:]:
				new_paths = []
				new_pos = []
				for ip, p in enumerate(pos):
					for (i2, j2, c2) in neig(*p):
						if c2 == c and (i2,j2) not in paths[ip]:
							pos[ip] = (i2, j2)
							new_paths.append(deepcopy(paths[ip]))
							new_paths[-1].add((i2, j2))
							new_pos.append((i2, j2))
						# end if
					# end for neig
				# end for p
				pos = new_pos
				paths = new_paths
				if len(pos) == 0:
					break
			# end for c
			if len(pos) > 0 and any([len(path) == len(word) for path in paths]):
				words_found.append(word)
		# end for word
		return words_found



# -------------------------------------------------------------------------------------------------------------------
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["eat", "oath","pea","rain"]

# board =[["a"]]
# words = ["b"]

# board = [["a","a"]]
# words = ["aaa"]

board =[["a","b"],
		["a","a"]]
words  = ["baa"]

print('board=\n')
for b in board:
	print(b)
print('words=\n', words)
print('output=\n')
sol = Solution()
print(sol.findWords(board, words))