class Solution:
    def findN(self, a, n, l, r):
        if l > r:
            return False
        mid = int((l + r) / 2)
        if a[mid] == n:
            return True
        if a[l] <= a[mid]:
            # lower part is the strictly increasing part
            if a[l] <= n <= a[mid]:
                return self.findN(a, n, l, mid - 1)
            else:
                return self.findN(a, n, mid + 1, r)
        else:
            # upper is the increasing part
            if a[mid] <= n <= a[r]:
                return self.findN(a, n, mid + 1, r)
            else:
                return self.findN(a, n, l, mid - 1)

import pytest
@pytest.mark.parametrize('a, n, expected', [
    ([2,3,4,6,7,-1,0,1], 3, True),
    ([2,3,4,6,7,-1,0,1], 0, True),
    ([2,3,4,6,7,-1,0,1], 10, False),
])
def test_sol(a, n, expected):
    sol = Solution()
    assert sol.findN(a, n, 0, len(a) - 1) == expected
