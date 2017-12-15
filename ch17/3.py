class Solution:
    def countZero(self, n):
        if n < 0:
            return -1
        i, cnt = 5, 0
        while i <= n:
            cnt += int(n/i)
            i *= 5
        return cnt

import pytest
@pytest.mark.parametrize('n, expected', [
        (0, 0), (-10, -1), (5, 1), (10, 2), (13, 2), (15, 3), (20, 4), (25, 6)
])
def test_count(n, expected):
    sol = Solution()
    assert sol.countZero(n) == expected
