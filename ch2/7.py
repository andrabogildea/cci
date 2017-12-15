def is_palindrom(head):
    stack = []
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        stack.append(slow.val)
        fast = fast.next.next
        slow = slow.next
    # check for case when list len is even
    if fast is not None:
        slow = slow.next
    while slow is not None:
        try:
            v = stack.pop()
        except:
            return False
        if slow.val != v:
            return False
        slow = slow.next
    return True

from sll import SLL
import pytest
@pytest.mark.parametrize('input, expected', [
    ([1], True),
    ([1,2], False),
    ([1,3,1], True),
    ([1,2,2,1], True),
    ([1,2,3,2,1], True),
    ([1,1,1,2,1,1], False)
])
def test_sol(input, expected):
    l = SLL()
    l._create(input)
    assert is_palindrom(l.head) == expected
