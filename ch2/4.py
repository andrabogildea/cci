def solution(node, x):
    beforeS, beforeE, afterS, afterE = None, None, None, None
    while node is not None:
        nxt = node.next
        node.next = None
        if node.val < x:
            if beforeS is None:
                beforeS = node
                beforeE = beforeS
            else:
                beforeE.next = node
                beforeE = beforeE.next
        else:
            if afterS is None:
                afterS = node
                afterE = afterS
            else:
                afterE.next = node
                afterE = afterE.next
        node = nxt
    if beforeS is None:
        return afterS
    beforeE.next = afterS
    return beforeS

def pp(node):
    l = []
    while node is not None:
        l.append(node.val)
        node = node.next
    return l

from sll import SLL
def test_sol():
    l = SLL()
    node = solution(l.head, 2)
    assert pp(node) == []
    l._create([6,5,7,4])
    node = solution(l.head, 3)
    assert pp(node) == [6,5,7,4]
    assert pp(solution(l.head, 4)) == [6,5,7,4]
    l = SLL()
    l._create([6,5,7,4])
    assert pp(solution(l.head, 5)) == [4,6,5,7]
    l = SLL()
    l._create([6,5,7,4])
    assert pp(solution(l.head, 7)) == [6,5,4,7]
