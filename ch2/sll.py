class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class SLL:
    def __init__(self):
        self.head = None

    def add(self, val):
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
        if val == head.val:
            tmp = head.next
            self.head = tmp
        else:
            prev = head
            head = head.next
            while head:
                if head.val == val:
                    print(prev.val )
                    prev.next = head.next
                    break
                head = head.next

    def print_list(self):
        head = self.head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l

    def _create(self, l):
        for item in l:
            self.add(item)

def pp(node):
    l = []
    while node is not None:
        l.append(node.val)
        node = node.next
    return l

def test_add():
    l = SLL()
    assert l.print_list() == []
    l.add(1)
    assert l.print_list() == [1]
    l.add(2)
    l.add(3)
    assert l.print_list() == [1,2,3]


def test_insert():
    l = SLL()
    l.insert(1, 1)
    assert l.print_list() == []
    l.insert(1,0)
    assert l.print_list() == [1]
    l._create([2,3,4])
    l.insert(9, 0)
    assert l.print_list() == [9, 1, 2, 3, 4]
    # insert on last existing position
    l.insert(8, 4)
    assert l.print_list() == [9, 1, 2, 3 ,8, 4]
    # insert in non existent position
    l.insert(7, 10)
    assert l.print_list() == [9, 1, 2, 3, 8, 4]
    l.insert(6, 6)
    # insert at the end
    assert l.print_list() == [9, 1, 2, 3, 8, 4, 6]

def test_remove():
    l = SLL()
    l._create([1,2,3,4,5])
    l.remove(1)
    assert l.print_list() == [2,3,4,5]
    l.remove(5)
    assert l.print_list() == [2,3,4]
    l.remove(3)
    assert l.print_list() == [2,4]
    l.remove(8)
    assert l.print_list() == [2,4]
