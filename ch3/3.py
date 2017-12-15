class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, val):
        if self.is_empty():
            self.stacks.append(Stack())
        current_stack = self.stacks[-1]
        if current_stack.size + 1 > self.capacity:
            current_stack = Stack()
            self.stacks.append(current_stack)
        current_stack.push(val)

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        current_stack = self.stacks[-1]
        try:
            res = current_stack.pop()
        except:
            self.stacks.pop()
            raise Exception('Empty Stack.')
        if current_stack.is_empty():
            self.stacks.pop()
        return res

    def is_empty(self):
        return len(self.stacks) == 0

    def popAt(index):
        if 0 > index or index >= len(self.stacks):
            raise Exception('Index out of range.')
        stack = self.stack[index]
        val = stack.pop()
        for i in range(index, len(self.stacks) - 1):
            self.stack[i].push(self.stacks[i+1].popBottom().val)
        return val


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def push(self, val):
        self.top = Node(val=val, next=self.top)
        if self.bottom is None:
            self.bottom = self.top
        self.size += 1

    def pop(self):
        if self.top is not None:
            tmp = self.top
            self.top = self.top.next
            # make bottom none if stack is empty
            if self.top is None:
                self.bottem = None
            self.size -= 1
            return tmp.val
        return None

    def popBottom(self):
        if self.bottom is not None:
            tmp = self.bottom
            self.bottom = self.bottom.next
            self.size -= 1
            return tmp
        return None

    def is_empty(self):
        return self.top is None:
