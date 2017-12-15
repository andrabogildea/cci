from collections import deque
class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return 'Node(val=%s)' % (self.val)

def from_bfs(l, node):
    if len(l) == 0:
        return None, None
    start = None
    head = Node(val=l[0])
    queue= deque([head])
    for i in range(2, len(l), 2):
        current_node = queue.popleft()
        if current_node.val == node:
            start = current_node
        if l[i-1] is not None:
            current_node.left = Node(val=l[i-1], parent=current_node)
            queue.append(current_node.left)
        if l[i] is not None:
            current_node.right = Node(val=l[i], parent=current_node)
            queue.append(current_node.right)
    return head, start

class Solution:
    def findNextInorder(self, node):
        if node is None:
            return None
        if node.right is not None:
            return self.leftmostNode(node.right)
        else:
            parent = node.parent
            while parent is not None and parent.right == node:
                node = parent
                parent = node.parent
            if parent is None:
                return None
            return parent.val

    def leftmostNode(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.val


# ------------------------Test--------------------
import pytest


@pytest.mark.parametrize('tree, node, expected', [
    ([], 1, None),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], 1, 2),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], 8, 10),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], 17, None),
    ([10,5,15,2,7,None,17,1,None,6,8,None,None,None,None,None,None,None,None], 7, 8),
])
def test_nextInorder(tree, node, expected):
    sol = Solution()
    tree, node = from_bfs(tree, node)
    assert sol.findNextInorder(node) == expected
