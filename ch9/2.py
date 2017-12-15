def countPaths(x, y, xs=0, ys=0, cache=None):
    if cache is None:
        cache = {(x,y) : 1}
    if xs > x or ys > y:
        return 0
    if cache.get((xs,ys), None) is None:
        cache[(xs, ys)] = countPaths(x, y, xs+1, ys) + countPaths(x,y, xs, ys+1)
    return cache[(xs,ys)]

import math
def countPathsMath(x,y):
    return math.factorial(x+y)/(math.factorial(x)*math.factorial(y))

import pytest
@pytest.mark.parametrize('x,y,res', [
    (1, 1, 2),
    (2, 2, 6),
    (5, 7, 792)
])
def test_countPaths(x, y, res):
    assert countPaths(x,y) == res
    assert countPathsMath(x,y ) == res


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)

    def isInList(self, list):
        for p in list:
            if self.x == p.x and self.y == p.y:
                return True
        return False

def findPath(x, y, locked, path=None, current=Point(0,0)):
    if path is None:
        path = []
    if current.x == x and current.y == y:
        path.append(current)
        return True
    if current.x > x or current.y > y or current.isInList(locked):
        return False
    exists = findPath(x, y, locked, path, Point(current.x+1, current.y))
    if exists:
        path.append(current)
    else:
        exists = findPath(x,y, locked, path,Point(current.x, current.y+1))
        if exists:
            path.append(current)
    return exists

def solution(x,y,locked):
    path = []
    findPath(x,y,locked,path)
    return path

@pytest.mark.parametrize('x,y,locked,expected', [
    (4,6,[Point(4,1)], []),
])
def test_sol(x,y,locked,expected):
    pass
