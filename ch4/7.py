from collections import deque
from utils import Node


class Solution:
    def findCommonAnecstor(self, tree, p, q):
        if not self.existsNode(tree, p):
            return None
        if not self.existsNode(tree, q):
            return None
        return self.findCommonAncestorHelper(tree, p, q)

    def findCommonAncestorHelper(self, tree, p, q):
        if tree is None or p is None or q is None:
            return None
        if tree == p or tree == q:
            return tree.val
        p_is_in_left = self.existsNode(tree.left, p)
        q_is_in_left = self.existsNode(tree.left, q)

        if p_is_in_left != q_is_in_left:
            return tree.val

        if (p_is_in_left and q_is_in_left) == True:
            return self.findCommonAncestorHelper(tree.left, p, q)
        return self.findCommonAncestorHelper(tree.right, p, q)

    def existsNode(self, tree, node):
        if tree is None or node is None:
            return False
        if node == tree:
            return True
        return self.existsNode(tree.left, node) or self.existsNode(tree.right, node)


def from_bfs(l, p, q):
    if len(l) == 0:
        return None, None, None
    p_node, q_node = None, None
    head = Node(val=l[0])
    queue= deque([head])
    for i in range(2, len(l), 2):
        current_node = queue.popleft()
        if current_node.val == p:
            p_node = current_node
        if current_node.val == q:
            q_node = current_node
        if l[i-1] is not None:
            current_node.left = Node(val=l[i-1])
            queue.append(current_node.left)
        if l[i] is not None:
            current_node.right = Node(val=l[i])
            queue.append(current_node.right)
    return head, p_node, q_node

# ------------------------Test-----------------------
import pytest
@pytest.mark.parametrize('tree, p, q, expected', [
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], 21, 5, None),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], 1, 5, 5),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], 2, 17, 10),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], 6, 8, 7),
])
def test_findCommonAncestor(tree, p, q, expected):
    sol = Solution()
    tree, p, q = from_bfs(tree, p, q)
    assert sol.findCommonAnecstor(tree, p, q) == expected
