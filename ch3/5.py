class Queue:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.input = []
        self.output = []
        self.size = 0
        for i in iterable:
            self.put(i)

    def put(self, val):
        self.input.append(val)
        self.size += 1

    def remove(self):
        if self.is_empty():
            return None
        if len(self.output) == 0:
            while self.input:
                self.output.append(self.input.pop())
        self.size -= 1
        return self.output.pop()

    def is_empty(self):
        return self.size == 0

def test_queue():
    q = Queue()
    assert q.remove() == None
    for i in range(3):
        q.put(i)
    assert q.remove() == 0

