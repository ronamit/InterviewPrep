class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_len = 2 * numRows - 2 if numRows > 2 else numRows
        n = len(s)
        # first line:
        out_s = s[:n:zigzag_len]
        # middle lines:
        for r in range(1, zigzag_len // 2):
            downs = s[r:n:zigzag_len]
            ups = s[(zigzag_len - r) : n : zigzag_len]
            for i, d in enumerate(downs):
                out_s += d
                if i < len(ups):
                    out_s += ups[i]
        # last line:
        if numRows > 1:
            out_s += s[(numRows - 1) : n : zigzag_len]
        return out_s
