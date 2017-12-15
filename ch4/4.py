from collections import deque


class Solution:
    def createLevelLists(self, tree):
        if tree is None:
            return []
        depth = 0
        to_visit, res = deque([tree]), []
        while len(to_visit) > 0:
            layer_res = []
            for i in range(len(to_visit)):
                current = to_visit.popleft()
                layer_res.append(current.val)
                if current.left is not None:
                    to_visit.append(current.left)
                if current.right is not None:
                    to_visit.append(current.right)
            res.append(layer_res)
        return res

# -------------------------Tests------------------------
import pytest
from utils import from_bfs

@pytest.mark.parametrize('input, expected', [
    ([1,2,None,3,None,4,None,None,None], [[1], [2], [3], [4]]),
    ([1,2,3,4,5,6,None,7,8,None,None,9,10,None,None,None,None,None,None,None,None], [[1], [2,3],[4,5,6],[7,8,9,10]])
])
def test_create(input, expected):
    sol = Solution()
    tree = from_bfs(input)
    assert sol.createLevelLists(tree) == expected
