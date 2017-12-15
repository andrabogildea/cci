class Stack:
    def __init__(self, iterator=None):
        if iterator is None:
            iterator = []
        self.s = []
        for i in iterator:
            self.push(i)

    def push(self, val):
        self.s.append(val)

    def pop(self):
        return self.s.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.s[-1]

    def is_empty(self):
        return len(self.s) == 0

def sort(stack):
    auxS = Stack()
    while not stack.is_empty():
        tmp = stack.pop()
        while not auxS.is_empty() and auxS.peek() > tmp:
            stack.push(auxS.pop())
        auxS.push(tmp)
    return auxS

import pytest
@pytest.mark.parametrize('input,expected', [
    (Stack(), []),
    (Stack([1,2]), [1,2]),
    (Stack([1,5,9,2,7,4,1,2,8,11]), [1,1,2,2,4,5,7,8,9,11])
])
def test_soltution(input, expected):
    assert sort(input).s == expected

