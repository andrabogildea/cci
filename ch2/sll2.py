#TODO: explore node as a struct

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        klass = self.__class__.__name__
        return '%s(%r, %r)' % (klass, self.val, self.next)


class LinkedList:
    def __init__(self, l=[]):
        self.head = None
        for x in reversed(l):
            self.insert(x, 0)

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = Node(val)

    def insert(self, val, pos):
        if pos == 0:
            tmp = Node(val)
            tmp.next = self.head
            self.head = tmp
        else:
            if self.head is None:
                return
            head = self.head
            ct = 1
            while head:
                if ct == pos:
                    tmp = Node(val)
                    tmp.next = head.next
                    head.next = tmp
                    break
                ct += 1
                head = head.next

    def remove(self, val):
        head = self.head
        if head is None:
            return
        if val == head.val:
            tmp = head.next
            self.head = tmp
        else:
            prev = head
            head = head.next
            while head:
                if head.val == val:
                    prev.next = head.next
                    break
                head = head.next

    def __repr__(self):
        klass = self.__class__.__name__
        return '%s(%r)' % (klass, self.head)




a = LinkedList(range(10))
print a
