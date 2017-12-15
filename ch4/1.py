class Solution:
    def isBalanced(self, tree, cache={}):
        if tree is None:
            return True
        if abs(self.height(tree.left) - self.height(tree.right)) > 1:
            return False
        return self.isBalanced(tree.left) and self.isBalanced(tree.right)

    def height(self, tree):
        if tree is None:
            return 0
        return 1 + max(self.height(tree.left), self.height(tree.right))

    def isBalanced2(self, node):
        if self.checkHeight(node) == -1:
            return False
        return True

    def checkHeight(self, node):
        if node == None:
            return 0

        # check if left is balanced
        lh = self.checkHeight(node.left)
        if lh == -1:
            return -1

        # check if right is balanced
        rh = self.checkHeight(node.right)
        if rh == -1:
            return -1

        # check if curr node is balanced
        if abs(rh-lh) > 1:
            return -1
        return max(rh, lh) + 1
# ----------------Tests----------------------
from utils import from_bfs
import pytest
@pytest.mark.parametrize('tree, expected', [
    ([1,2,3,4,5,6,7,None,8,None,None,None,None,None,9], True),
    ([1,2,3,4,5,6,7,10,8,None,None,None,None,None,9,11,None, None, None], False),
])
def test_isBalanced(tree, expected):
    sol = Solution()
    tree = from_bfs(tree)
    assert sol.isBalanced(tree) == expected
    assert sol.isBalanced2(tree) == expected
