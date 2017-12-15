from stack import Stack

class Tower:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self, val):
        return self.stack.pop()

    def moveTopTo(self, tower):
        tower.push(self.stack.pop())

    def moveNTo(self, n, destT, auxT):
        if n == 0:
            return
        self.moveNTo(n-1, auxT, destT)
        self.moveTopTo(destT)
        auxT.moveNTo(n-1, destT, self)

def sol(disks):
    t_nr = 3
    towers = []
    for i in range(t_nr):
        towers.append(Tower())
    for i in range(disks, 0, -1):
        towers[0].push(i)
    towers[0].moveNTo(disks, towers[2], towers[1])
    return towers[2]

import pytest

@pytest.mark.parametrize('input,expected', [
    (3, [3,2,1]),
    (0, []),
    (7, [7,6,5,4,3,2,1])
])
def test_sol(input, expected):
    assert sol(input).stack == expected

# def move(nr_disks, start, dest, aux):
#     if nr_disks == 1:
#         disk = towers[start].pop()
#         towers[dest].append(disk)
#         return
#     move(nr_disks - 1, start, aux, dest)
#     move(1, start, dest, aux)
#     move(nr_disks - 1, aux, dest, start)


# def test_sol():
#     move(6, 0, 2, 1)
#     print(towers[0], towers[1], towers[2])
#     assert True == False
