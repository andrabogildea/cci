class Solution:
    def paintFill(self, screen, l, c, colour):
        if screen[l][c] == colour:
            return
        self.paint(screen, l, c, colour, screen[l][c])

    def paint(self, screen, l, c, newcol, oldcol):
        if l < 0 or c < 0 or l >= len(screen) or c >= len(screen[0]) or screen[l][c] != oldcol:
            return
        screen[l][c] = newcol
        self.paint(screen, l-1, c, newcol, oldcol)
        self.paint(screen, l, c+1, newcol, oldcol)
        self.paint(screen, l+1, c, newcol, oldcol)
        self.paint(screen, l, c-1, newcol, oldcol)

import pytest
@pytest.mark.parametrize('screen, l, c, col, expected', [
    ([[0,0,0,1], [0,0,0,1], [0,0,1,1], [1,1,1,1]], 2, 2, 2, [[0,0,0,2], [0,0,0,2], [0,0,2,2], [2,2,2,2]])
])
def test_sol(screen, l, c, col, expected):
    sol = Solution()
    sol.paintFill(screen, l, c, col)
    assert screen == expected
