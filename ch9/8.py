class Solution:
    def countWaysToN(self, n):
        if n == 0:
            return 0
        coins = [25, 10, 5, 1]
        return self.countWays(n, 0, coins)

    def countWays(self, n, coin, coins):
        if n == 0:
            return 1
        if coin >= len(coins):
            return 0
        ct, ways = 0, 0
        while coins[coin] * ct <= n:
            ways += self.countWays(n - coins[coin] * ct, coin + 1, coins)
            ct += 1
        return ways

import pytest
@pytest.mark.parametrize('n, expected', [
    (0, 0),
    (1, 1),
    (2, 1),
    (5, 2),
    (10, 4),
    (15, 6)
])
def test_sol(n, expected):
    s = Solution()
    assert s.countWaysToN(n) == expected
