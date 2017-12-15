import threading


class Chopstick:
    def __init__(self):
        self.lock = threading.Lock()

    def pickUp(self):
        return self.lock.acquire(blocking=False)

    def putDown(self):
        self.lock.release()

class Philosopher:
    def __init__(self, right, left):
        self.bites = 10
        self.left = left
        self.right = right

    def eat(self):
        if self.pickUp():
            self.chew()
            self.putDown()

    def chew(self):
        print("I'm chewing")

    def pickUp(self):
        if not self.right.pickUp():
            return False
        if not self.left.pickUp():
            self.right.pickUpe.putDown()
            return False
        return True

    def putDown(self):
        self.right.putDown()
        self.left.putDown()

    def run(self):
        for i in range(self.bites):
            self.eat()

def test():
    c1, c2, c3, c4 = Chopstick(), Chopstick(), Chopstick(), Chopstick()
    p1 = Philosopher(c4, c1)
    p2 = Philosopher(c1, c2)
    p3 = Philosopher(c2, c3)
    p4 = Philosopher(c3, c4)
    t1 = threading.Thread(target=p1.run)
    t2 = threading.Thread(target=p2.run)
    t3 = threading.Thread(target=p3.run)
    t4 = threading.Thread(target=p4.run)
    threads = [t1, t2, t3, t4]
    for t in threads:
        t.start()

test()
