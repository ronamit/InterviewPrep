

def generate(self, numRows: 'int') -> 'List[List[int]]':
    out = []
    for irow in range(numRows):
        out += [[1 for _ in range(irow+1)]]
        for j in range(1, irow):
            out[irow][j] = out[irow-1][j] + out[irow-1][j-1]
    return out




self = None
numRows = 5
print(generate(self, numRows))
