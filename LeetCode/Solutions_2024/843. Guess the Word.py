# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        pass


class Solution:
    def count_matches(self, w1: str, w2: str) -> int:
        cnt = 0
        for i, c in enumerate(w1):
            cnt += w2[i] == c
        return cnt

    def findSecretWord(self, words: list[str], master: Master) -> None:
        # Idea: build a graph between all words, with edge weights = the number of char matches/  O(n^2)
        # Find in the graph the node with the most unique edge values and use it as guess word (use heap?)
        # eliminate from the graph all the words that don't match, O(n^2) remove the edges
        # repeat

        n = len(words)
        word_len = len(words[0])
        matches = [[] for _ in range(n)]
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                match_count = self.count_matches(words[i1], words[i2])
                matches[i1].append((i2, match_count))
                matches[i2].append((i1, match_count))

        discarded = set()  # indexes of discarded words (can't be the secret)

        for _ in range(30):
            max_uniq = -float("inf")
            i_max_uniq = 0
            for i_word in range(n):
                if i_word in discarded:
                    continue
                cur_match_counts = []
                for i_word2, match_cnt in matches[i_word]:
                    if i_word2 in discarded:
                        continue
                    cur_match_counts.append(match_cnt)
                n_uniq_counts = len(set(cur_match_counts))
                if n_uniq_counts > max_uniq:
                    max_uniq = n_uniq_counts
                    i_max_uniq = i_word
            # gues the word with most uniq match counts
            guessed_word = words[i_max_uniq]
            guessed_word_matches = master.guess(guessed_word)
            print("Guess: ", guessed_word, ", matches: ", guessed_word_matches)
            if guessed_word_matches == word_len:
                print("Found secret")
                return

            discarded.add(i_max_uniq)  # the guessed word can't be the secret if wrong
            # update discard (word's that can't be the secret)
            for i_word in range(n):
                if i_word not in discarded and self.count_matches(guessed_word, words[i_word]) != guessed_word_matches:
                    discarded.add(i_word)
