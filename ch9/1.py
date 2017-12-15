def countWays(n, cache=None):
    if cache == None:
        cache = {0:1}
    if n < 0:
        return 0
    if cache.get(n, None) is None:
        cache[n] = countWays(n-1) + countWays(n-2) + countWays(n-3)
    return cache[n]

def countWaysB(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return countWaysB(n-1) + countWaysB(n-2) + countWaysB(n-3)
import pytest
@pytest.mark.parametrize('n, expected', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 7)
])
def test_sol(n, expected):
    assert countWays(n) == expected
    assert countWaysB(n) == expected

