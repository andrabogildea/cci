import pytest
from copy import copy
from utils import from_bfs


class Solution:
    def findPathWithSum(self, tree, target_sum, path=None, solutions=None):
        if tree is None:
            return []
        if path is None:
            path = []
        if solutions is None:
            solutions = []
        path.append(tree.val)
        sum = 0
        for i in range(len(path) - 1, -1, -1):
            sum += path[i]
            if sum == target_sum:
                self.printPath(path, i, len(path) - 1, solutions)

        self.findPathWithSum(tree.left, target_sum, path, solutions)
        self.findPathWithSum(tree.right, target_sum, path, solutions)

        path.pop()

    def printPath(self, path, start, end, solutions):
        p = []
        for i in range(start, end + 1):
            p.append(path[i])
        solutions.append(p)
        print(p)

@pytest.mark.parametrize('tree, target_sum, expected', [
    ([2,3,4,1,2,-2,3,-1,-2,None,-1,None,None,1,None,1, None,None,None,None,None,None,None,None], 4, 7),
    ([2,3,4,1,2,-2,3,-1,-2,None,-1,None,None,1,None,1, None,None,None,None,None,None,None,None], 15, 0),
    ([], 3, 0),
    ([3,3,None,None,None], 3, 2)
])
def test_findPaths(tree, target_sum, expected):
    sol = Solution()
    tree = from_bfs(tree)
    solutions = []
    sol.findPathWithSum(tree, target_sum, solutions=solutions)
    assert len(solutions) == expected
# 3 1
# 3 1 -1 1
# 2 3 1 -2
# 3 2 -1
# 2 4 -2
# 4
# 3 1
