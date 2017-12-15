import pytest
from utils import from_bfs


class Solution:
    def isSubtree(self, t1, t2):
        if t2 is None:
            return True
        return self.isSubtreeHelper(t1, t2)

    def isSubtreeHelper(self, t1, t2):
        if t1 is None:
            return False
        if t1.val == t2.val:
            if self.matchTrees(t1, t2):
                return True
        return self.isSubtreeHelper(t1.left, t2) or self.isSubtreeHelper(t1.right, t2)

    def matchTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if (t1 is None and t2 is not None) or (t1 is not None and t2 is None):
            return False
        if t1.val != t2.val:
            return False
        return self.matchTrees(t1.left, t2.left) and self.matchTrees(t1.right, t2.right)

# ----------------------------------Tests------------------------------
@pytest.mark.parametrize('t1, t2, expected', [
    ([], [2, None, None], False),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], [], True),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], [15,17,17,None,None], False),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], [15,None,17,None,None], True),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], [5,2,7,1,None,6,8,None,None,None,None], True),
])
def test_isSubtree(t1, t2, expected):
    sol = Solution()
    t1 = from_bfs(t1)
    t2 = from_bfs(t2)
    assert sol.isSubtree(t1, t2) == expected
