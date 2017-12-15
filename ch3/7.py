class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self, iterator=None):
        if iterator is None:
            iterator = []
        self.head = None
        self.tail = None
        for i in iterator:
            self.enqueue(i)

    def enqueue(self, val):
        if self.tail is None:
            self.tail = Node(val=val)
            self.head = self.tail
        else:
            self.tail.next = Node(val=val)
            self.tail = self.tail.next

    def dequeue(self):
        if self.isEmpty():
            return None
        tmp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return tmp.val

    def isEmpty(self):
        return self.head is None

    def peek(self):
        if self.isEmpty()
            return None
        return self.head.val



# ------------------------------------------
class Dog:
    def __init__(self, id):
        self.id = id

class Cat:
    def __init__(self, id):
        self.id = id

class Animal:
    def __init__(self, animal, order):
        self.animal = animal
        self.order = order

class AnimalQueue:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.order = 0

    def isOlderThan(self, animal):
        return self.order < animal.order

    def enqueue(self, animal):
        a = Animal(animal, self.order)
        self.order += 1
        if isinstance(animal, Cat):
            self.cats.enqueue(a)
        elif isinstance(animal, Dog):
            self.dogs.enqueue(a)

    def dequeueAny(self):
        if self.cats.isEmpty():
            return self.dequeueDog()
        if self.dogs.isEmpty():
            return self.dequeueCat()
        if self.cats.peek().isOlderThan(self.dogs.peek):
            return self.dequeueCat()
        return self.dequeueDog()

    def dequeueCat(self):
        if self.cats.isEmpty():
            return None
        return self.cats.dequeue()

    def dequeueDog(self):
        if self.dogs.isEmpty():
            return None
        return self.dogs.dequeue()
