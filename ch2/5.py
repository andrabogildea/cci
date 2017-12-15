def sum(node1, node2):
    head = Node()
    end = head
    carry = 0
    while node1 is not None and node2 is not None:
        s = node1.val + node2.val + carry
        carry = int(s/10)
        end.next = Node(val=s%10)
        end = end.next
        node1 = node1.next
        node2 = node2.next
    while node1 is not None:
        s = node1.val + carry
        carry = int(s/10)
        end.next = Node(val=s%10)
        end = end.next
        node1= node1.next
    while node2 is not None:
        s = node2.val + carry
        carry = int(s/10)
        end.next = Node(val=s%10)
        end = end.next
        node2 = node2.next
    if carry > 0:
        end.next = Node(val=carry)
    return head.next

def sum2(node1, node2):
    head = Node()
    end = head
    carry = 0
    while node1 is not None or node2 is not None:
        s = carry
        if node1 is not None:
            s += node1.val
            node1 = node1.next
        if node2 is not None:
            s += node2.val
            node2 = node2.next
        carry = int(s/10)
        end.next = Node(val=s%10)
        end = end.next
    if carry > 0:
        end.next = Node(val=carry)
    return head.next

# --------------------------------------------------------
def sumR(node1, node2):
    size1, size2 = size(node1), size(node2)
    if size1 > size2:
        node2 = add_padding(node2, size1-size2)
    if size2 > size1:
        node1 = add_padding(node1, size2-size1)
    return sumEq(node1, node2)

def sumEq(node1, node2):
    result = sumRec(node1, node2)
    carry = int(result.val/10)
    result.val = result.val%10
    if carry > 0:
        tmp = Node(val=carry, next=result)
        result = tmp
    return result

def sumRec(node1, node2):
    if node1.next is None and node2.next is None:
        return Node(val=node1.val+node2.val)
    s = node1.val + node2.val
    result = sumRec(node1.next, node2.next)
    carry = int(result.val/10)
    result.val = result.val % 10
    s += carry
    return Node(val=s, next=result)

def size(node):
    s = 0
    while node is not None:
        s += 1
        node = node.next
    return s

def add_padding(node, x):
    while x > 0:
        tmp = Node(val=0, next=node)
        node = tmp
        x -= 1
    return node



from sll import Node, SLL, pp
import pytest
@pytest.mark.parametrize('input, expected', [
    (([], [1,2]), [1,2]),
    (([9,9,9,2], [1]), [0,0,0,3]),
    (([5,4,5], [1,2,5]), [6,6,0,1])])
def test_sum(input, expected):
    li1 = SLL()
    li1._create(input[0])
    li2 = SLL()
    li2._create(input[1])
    assert pp(sum(li1.head, li2.head)) == expected
    assert pp(sum2(li1.head, li2.head)) == expected

@pytest.mark.parametrize('input, expected', [
    (([], [1,2]), [1,2]),
    (([2,9,9,9], [1]), [3,0,0,0]),
    (([5,4,5], [5,2,1]), [1,0,6,6])])
def test_sum(input, expected):
    li1 = SLL()
    li1._create(input[0])
    li2 = SLL()
    li2._create(input[1])
    assert pp(sumR(li1.head, li2.head)) == expected
