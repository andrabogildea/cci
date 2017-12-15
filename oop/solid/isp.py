import time


# class Timer:
#     def register(self, timeout, timerClient):
#         print('Waiting for ', timeout, 'minuteds')
#         timerClient.timeout()


# class TimerClient:
#     def timeout(self):
#         print(self.__class__.__name__ + ':''I timedout')


# class Door(TimerClient):
#     def __init__(self):
#         self.isOpend = False

#     def open(self):
#         self.isOpen = True
#         print(self.__class__.__name__ + ':' +' Door was open')

#     def close(self):
#         self.isOpen = False
#         print(self.__class__.__name__ + ':'+ ' Door was closed')

#     def doorIsOpen(self):
#         return self.isOpen == True

# class TimedDoor(Door):
#     def __init__(self, timer):
#         super().__init__()
#         self.timer = timer

#     def open(self):
#         super().open()
#         self.timer.register(3, self)

# def main():
#     timer = Timer()
#     td = TimedDoor(timer)
#     td.open()
#     td.close()

# main()

 class Timer:
    def register(self, timeout, timerClient):
        print('Waiting', timeout, 'minuteds')
        timerClient.timeout()


class TimerClient:
    def timeout(self):
        print('I timedout')


class Door:
    def __init__(self):
        self.isOpen = False

    def open(self):
        self.isOpen = True
        print(self.__class__.__name__ + ':' + 'Door was open')

    def close(self):
        self.isOpen = False
        print(self.__class__.__name + ':' + 'Door was closed')

    def doorIsOpen(self):
        return self.isOpen == True


class TimedDoor(Door):
    def __init__(self, dta, timeout):
        super().__init__()
        self.dta = dta
        self.timeout = timeout

    def doorTimeout(self):
        if self.doorIsOpen():
            print(self.__class__.__name__ + ': I timedout')

    def open(self):
        super().open()
        self.timeout(2, self.dta)

class DoorTimerAdapter(TimerClient):
    def __init__(self, timeddoor):
        self.timeddoor = timeddoor

    def timeout(self):
        self.timeddoor.doorTimeout()

def main():
    timer = Timer()
    dta = DoorTimerAdapter(td)
    td = TimedDoor()
main()
