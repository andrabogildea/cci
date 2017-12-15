class Solution:
    def max(self, x, y):
       max_nr = {
           1: x,
           0: y
       }
       return max_nr[self.greater_than(x, y)]

    def max2(self, x, y):
       sign = self.greater_than(x, y)
       flipped = sign^1
       return x * sign + y * flipped

    def greater_than(self, x, y):
        return int(x > y)

import pytest
@pytest.mark.parametrize('x, y, expected', [
    (-1, 2, 2), (3, 3, 3), (-2, -4, -2), (20, 1, 20)
])
def test_sol(x, y, expected):
    sol = Solution()
    assert sol.max(x, y) == expected
    assert sol.max2(x, y) == expected
