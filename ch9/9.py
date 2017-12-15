from copy import copy


class Solution:
    def placeQueens(self):
        res, sol = [], [-1] * 8
        self.place(sol, 0, res)
        return res

    def place(self, cols, row, res):
        if row == 8:
            res.append(copy(cols))
            return
        for c in range(8):
            if self.isValid(cols, row, c):
                cols[row] = c
                self.place(cols, row + 1, res)

    def isValid(self, columns, row, c):
        for i in range(row):
            c2 = columns[i]
            # check column
            if c == c2:
                return False
            # check diagonal
            if abs(c2 - c) == row - i:
                return False
        return True

def test_sol():
    res = Solution().placeQueens()
    assert len(res) == 92
