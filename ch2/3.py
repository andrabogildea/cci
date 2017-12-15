def delete_node(node):
    # if node is the last one, make it dummy
    if node is None or node.next is None:
        return
    node.val = node.next.val
    prev = node
    node = node.next
    prev.next = node.next

from sll import SLL

def test_sol():
    l = SLL()
    l._create([1,2,3,4,5])
    delete_node(l.head.next.next)
    assert l.print_list() == [1,2,4,5]
    delete_node(l.head.next.next.next)
    assert l.print_list() == [1,2,4,5]
