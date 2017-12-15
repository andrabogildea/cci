class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        for i in iterable:
            self.push(i)

    def push(self, val):
        self.top = Node(val=val, next=self.top)

    def pop(self):
        if self.top is not None:
            tmp = self.top
            self.top = self.top.next
            return tmp.val
        return None

    def peek(self):
        if self.top is not None:
            return self.top.val
        return None

    def __repr__(self):
        pass
