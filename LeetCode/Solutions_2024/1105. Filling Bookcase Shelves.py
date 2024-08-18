from functools import cache


class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:

        @cache
        def get_min_height(i: int, w: int, h: int) -> int:
            nonlocal books, shelfWidth
            if i == len(books):
                return h
            book_w, book_h = books[i]
            h_if_new_shelf = h + get_min_height(i + 1, shelfWidth - book_w, book_h)
            if book_w > w:
                return h_if_new_shelf
            h_if_same_shelf = get_min_height(i + 1, w - book_w, max(h, book_h))
            return min(h_if_same_shelf, h_if_new_shelf)

        return get_min_height(0, shelfWidth, 0)
