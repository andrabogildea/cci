class Solution:
    def swap(self, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b

import pytest
@pytest.mark.parametrize('a, b', [
    (-1, -5), (0, 21), (-15, 3), (21, 22)
])
def test_swap(a, b):
    sol = Solution()
    assert sol.swap(a, b) == (b, a)
