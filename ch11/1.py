class Solution:
    def merge(self, a, b):
        curra, currb = len(a) - 1, len(b) - 1
        curr = len(a) + len(b) - 1
        a.extend([0]* len(b))
        while curra >= 0 and currb >= 0:
            if a[curra] >= b[currb]:
                a[curr] = a[curra]
                curr -= 1
                curra -= 1
            else:
                a[curr] = b[currb]
                curr -= 1
                currb -= 1
        while currb >= 0:
            a[curr] = b[currb]
            curr -= 1
            currb -= 1
        return a

import pytest
@pytest.mark.parametrize('a, b, newa', [
    ([1, 2, 5, 6, 8], [5, 9] , [1, 2, 5, 5, 6, 8, 9]),
    ([2, 3, 5, 6], [1, 4], [1,2,3,4,5,6]),
    ([1,3,5], [2, 3, 5, 6, 6, 7], [1,2,3,3,5,5,6,6,7])
])
def test_solution(a, b, newa):
    sol = Solution()
    assert sol.merge(a, b) == newa
