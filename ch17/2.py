class Solution:
    def hasWon(self, board):
        n = len(board)
        if n == 0 or len(board[0]) != n:
            return False
        col, row = 0, 0

        # check rows
        for row in range(n):
            if board[row][0] != 2:
                for col in range(1, n):
                    if board[row][col] != board[row][col-1]:
                        break
                    if col == n - 1:
                        print(1)
                        return True

        # check cols
        for col in range(n):
            if board[0][col] != 2:
                for row in range(1, n):
                    if board[row][col] != board[row-1][col]:
                        break
                    if row == n-1:
                        print(col)
                        print(2)
                        return True

        # check diagonl
        if board[0][0] != 2:
            for row in range(1, n):
                if board[row][row] != board[row-1][row-1]:
                    break
                if row == n - 1:
                    print(3)
                    return True

        # check other diagonal
        if board[0][n-1] != 2:
            for i in range(1, n):
                if board[i][n-1-i] != board[i-1][n-1-i-1]:
                    break
                if i == n-1:
                    print(4)
                    return True
        return False

import pytest

@pytest.mark.parametrize('board, result', [
    ([[1]], False),
    ([[1,0,1], [1,0,0], [2, 1, 0]], False),
    ([[1,0,1], [1,0,0], [1,0,2]], True)
])
def test_hasWon(board, result):
    sol = Solution()
    assert sol.hasWon(board) == result
