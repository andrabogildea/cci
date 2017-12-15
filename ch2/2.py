def kth_elment_from_end(head, k):
    if k < 1:
        return -1
    if head is None:
        return -1
    current = head
    ct = 0
    while current:
        if k == ct:
            break
        current = current.next
        ct += 1
    if ct < k:
        return -1
    print(ct)
    while current:
        current = current.next
        head = head.next
    return head.val

from sll import SLL
def test_sol():
    l = SLL()
    l._create([1,2,3,4,5,6,7,8,9])
    assert kth_elment_from_end(l.head, 1) == 9
    assert kth_elment_from_end(l.head, 3) == 7
    assert kth_elment_from_end(l.head, 9) == 1
    assert kth_elment_from_end(l.head, 21) == -1
