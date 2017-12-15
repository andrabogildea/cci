def find_cycle_head(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast.val == slow.val:
            break
    if fast is None or fast.next is None:
        return fast
    while head.val != slow.val:
        head = head.next
        slow = slow.next
    return head.val


import pytest
from sll import SLL, pp

def CLL(sll, n):
    el = sll.head
    while el.next:
        el = el.next
    last = el
    el = sll.head
    for _ in range(n):
        el = el.next
    last.next = el
    return sll


def pr(el, n):
    x = el
    for _ in range(n):
        print(x.val)
        x = x.next

@pytest.mark.parametrize('range,cycle,expected', [
    (range(10), 3, 3),
    (range(100), 10, 10),
    (range(100), 90, 90),
    (range(100), 0, 0),
    (range(100), 99, 99),
])
def test_sol(range, cycle, expected):
    x = SLL()
    x._create(range)
    x = CLL(x, cycle)
    pr(x.head, 30)
    assert find_cycle_head(x.head) == expected
