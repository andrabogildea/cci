class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self, iterable=[]):
        self.min = [99999]
        self.top = None
        for i in iterable:
            self.push(i)

    def push(self, val):
        current_min = self.min[-1]
        new_min = min(current_min, val)
        if new_min <= current_min:
            self.min.append(new_min)
        self.top = Node(val=val, next=self.top)

    def pop(self, default=None):
        if self.top is not None:
            tmp = self.top
            self.top = self.top.next
            if tmp.val == self.min[-1]:
                self.min.pop()
            return tmp.val
        return default

    def peek(self):
        if self.top is not None:
            return self.top.val
        return None

    def min_val(self):
        return self.min[-1]


def test_sol():
    s = Stack([1,3,5,6,1,3,2])
    assert s.min_val() == 1
    for i in range(3):
        s.pop()
    assert s.peek() == 6
    assert s.min_val() == 1
