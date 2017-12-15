from utils import Node, inorder


class Solution:
    def createMinimalBST(self, l):
        if len(l) == 0:
            return None
        return self.createMinimal(l, 0, len(l) - 1)

    def createMinimal(self, l, left, right):
        if right < left:
            return None
        mid = int((left + right) / 2)
        node = Node(l[mid])
        node.left = self.createMinimal(l, left, mid-1)
        node.right = self.createMinimal(l, mid + 1, right)
        return node

# ------------------------Tests-------------------------------
import pytest
@pytest.mark.parametrize('l, expected', [
    ([1,2,3,4], [1,2,3,4]),
    ([1], [1]),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [1,2,3,4,5,6,7,8,9,10,11,12,13,14])
])
def test_minimalbst(l, expected):
    sol = Solution()
    tree = sol.createMinimalBST(l)
    assert inorder(tree) == expected
