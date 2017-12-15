from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def from_bfs(l):
    if len(l) == 0:
        return None
    head = Node(val=l[0])
    queue= deque([head])
    for i in range(2, len(l), 2):
        current_node = queue.popleft()
        if l[i-1] is not None:
            current_node.left = Node(val=l[i-1])
            queue.append(current_node.left)
        if l[i] is not None:
            current_node.right = Node(val=l[i])
            queue.append(current_node.right)
    return head


def inorder(node, res=None):
    if node is None:
        return []
    if res is None:
        res = []
    inorder(node.left, res)
    res.append(node.val)
    inorder(node.right, res)
    return res

def inorder_gen(node):
    if Node is None:
        yield None
    inorder(node.left, res)
    yield node.val
    inorder(node.right, res)

def preorder(node, res=None):
    if node is None:
        return []
    if res is None:
        res = []
    res.append(node.val)
    preorder(node.left, res)
    preorder(node.right, res)
    return res

def preorder_gen(node):
    if Node is None:
        yield None
    yield node.val
    preorder(node.left, res)
    preorder(node.right, res)

def postorder(node, res=None):
    if node is None:
        return []
    if res is None:
        res = []
    postorder(node.left, res)
    postorder(node.right, res)
    res.append(node.val)
    return res

def postorder_gen(node):
    if Node is None:
        yield None
    postorder(node.left, res)
    postorder(node.right, res)
    yield node.val


def test_1():
    l = [1,2,3,4,5,6,7,8,None,9,None,None,None,None,None,None,None,None,10,None,None]
    tree = from_bfs(l)
    assert tree.val == 1
    assert inorder(tree) == [8,4,2,9,10,5,1,6,3,7]
    assert preorder(tree) == [1,2,4,8,5,9,10,3,6,7]
    assert postorder(tree) == [8,4,10,9,5,2,6,7,3,1]
