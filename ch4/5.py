class Solution:
    def checkBST(self, tree, largerThan=float('-inf'), smallerThan=float('inf')):
        if tree is None:
            return True
        if tree.val <= largerThan or tree.val > smallerThan:
            print(tree.val, largerThan, smallerThan)
            return False
        return self.checkBST(tree.left, largerThan, tree.val) and self.checkBST(tree.right, tree.val, smallerThan)

# -------------------------Test-----------------------------------
import pytest
from utils import from_bfs


@pytest.mark.parametrize('tree, expected', [
    ([20,10,20,5,15,None,None,3,7,None,17,None,None,None,None,None,None], False),
    ([], True),
    ([20,10,30,None,25,None,None,None,None], False),
    ([20,20,30,19,None,None,None,None,None], True),
    ([7,3,10,1,5,8,12,None,2,4,6,None,9,None,None,None,None,None,None,None,None,None,None], True)
])
def test_checkBst(tree, expected):
    sol = Solution()
    tree = from_bfs(tree)
    assert sol.checkBST(tree) == expected
