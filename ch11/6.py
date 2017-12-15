class Solution:
    def searchInMatrix(self, matrix, target):
        if target is None or len(matrix) == 0:
            return False
        return self.search(matrix, target, 0, len(matrix) * len(matrix[0]) - 1)

    def search(self, matrix, target, l, r):
        if l > r:
            return False
        mid = int((l + r) / 2)
        midrow, midcol = int(mid/len(matrix[0])), mid % len(matrix[0])
        if matrix[midrow][midcol] == target:
            return True
        if matrix[midrow][midcol] > target:
            return self.search(matrix, target, l, mid - 1)
        return self.search(matrix, target, mid + 1, r)

import pytest
@pytest.mark.parametrize('matrix, target, res', [
    ([[2,4,6,7], [8,9,10,11], [12,13,14,15], [16,17,18,19], [20, 21, 22, 23]], 9, True),
    ([[2,4,6,7], [8,9,10,11], [12,13,14,15], [16,17,18,19], [20, 21, 22, 23]], 18, True),
    ([[2,4,6,7], [8,9,10,11], [12,13,14,15], [16,17,18,19], [20, 21, 22, 23]], 50, False),
])
def test_sol(matrix, target, res):
    sol = Solution()
    assert sol.searchInMatrix(matrix, target) == res
