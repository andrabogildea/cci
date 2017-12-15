def solution(head):
    if head is None:
        return head
    current = head
    while current:
        runner = current.next
        prev = current
        while runner:
            if current.val == runner.val:
                prev.next = runner.next
            else:
                prev = runner
            runner = runner.next
        current = current.next
    return head

def pprintl(head):
    l = []
    while head is not None:
        l.append(head.val)
        head = head.next
    return l

from sll import SLL
def test_sol():
    l = SLL()
    l._create([1])
    l = solution(l.head)
    assert pprintl(l) == [1]
    l = SLL()
    l._create([1,2,1])
    l = solution(l.head)
    assert pprintl(l) == [1,2]
    l = SLL()
    l._create([1,2,1,1,2,5,5,6,1])
    l = solution(l.head)
    assert pprintl(l) == [1,2,5,6]
