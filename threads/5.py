import threading
import time


class Foo:
    def __init__(self):
        self.l2 = threading.Event()
        self.l3 = threading.Event()

    def first(self):
        print('Start first')
        time.sleep(5)
        self.l2.set()
        print('End first')

    def second(self):
        self.l2.wait()
        print('Start second')
        time.sleep(5)
        self.l3.set()
        print('End second')

    def third(self):
        self.l3.wait()
        print('Start third')
        time.sleep(5)
        self.l3.set
        print('End third')

def test():
    foo = Foo()
    t1 = threading.Thread(target=foo.first)
    t2 = threading.Thread(target=foo.second)
    t3 = threading.Thread(target=foo.third)
    t3.start()
    t2.start()
    t1.start()

test()
