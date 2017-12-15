from collections import deque
class Employee:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.available = True

    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def isInCall(self):
        return not self.available

    def enterCall(self):
        self.available = False

    def exitCall(self):
        self.availabel = True


class Director:
    def __init__(self, employee_fatory=Employee, name):
        self.employee = Employee(name=name, rank=3)

    def getName(self):
        return self.employee.getName()

    def getRank(self):
        return self.employee.getRank()

    def isInCall(self):
        return self.employee.isInCall()

    def enterCall(self):
        self.employee.enterCall()

    def exitCall(self):
        self.employee.exitCall()


class Manager:
    def __init__(self, employee_fatory=Employee, name):
        self.employee = Employee(name=name, rank=2)

    def getName(self):
        return self.employee.getName()

    def getRank(self):
        return self.employee.getRank()

    def isInCall(self):
        return self.employee.isInCall()

    def enterCall(self):
        self.employee.enterCall()

    def exitCall(self):
        self.employee.exitCall()


class Respondant:
    def __init__(self, employee_fatory=Employee, name):
        self.employee = Employee(name=name, rank=2)

    def getName(self):
        return self.employee.getName()

    def getRank(self):
        return self.employee.getRank()

    def isInCall(self):
        return self.employee.isInCall()

    def enterCall(self):
        self.employee.enterCall()

    def exitCall(self):
        self.employee.exitCall()


class Caller:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Call:
    def __init__(self, caller):
        self.caller = caller
        self.employee = None

    def pickUp(self, empl):
        self.employee = empl
        empl.enterCall()

    def hangUp(self):
        self.employee.exitCall()
        self.employee = None

    def isWaiting(self):
        return self.employee is None

    def getResoponder(self):
        return self.employee


class Dispatch:
    def __init__(self, employees, call_factory):
        self.employees = employees
        self.call_queues = [[],[],[]]

    def relay(self, caller):
        self.levels = [1,2,3]
        call = call_factory(caller)
        self.dispatch(call)


    def dispatch(self, call):
        if call.isWaiting

