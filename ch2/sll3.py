#TODO: explore node as a struct


class EmptyLinkedList:
    def append(self, val):
        return MultiLinkedList(val, EmptyLinkedList())

    def insert(self, pos, val):
        if pos == 0:
            return MultiLinkedList(val, EmptyLinkedList())
        return self

    def remove(self, val):
        return self

    def __repr__(self):
        klass = self.__class__.__name__
        return '%s()' % klass


class MultiLinkedList:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def append(self, val):
        return MultiLinkedList(self.val, self.next.append(val))

    def insert(self, pos, val):
        if pos == 0:
            return MultiLinkedList(val, self)
        if pos == 1:
            return MultiLinkedList(self.val, MultiLinkedList(val, self.next))
        return MultiLinkedList(self.val, self.next.insert(pos-1, val))

    def remove(self, val):
        if val == self.val:
            return self.next
        return MultiLinkedList(self.val, self.next.remove(val))

    def __repr__(self):
        klass = self.__class__.__name__
        return '%s(%r, %r)' % (klass, self.val, self.next)




l = EmptyLinkedList()
l = l.append(1)
l = l.append(2)
l = l.append(10)
l = l.insert(2, 7)
print l
