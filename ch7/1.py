class Line:
    def __init__(self, p1, p2):
        # pb when lines are vertical
        self.slope = (p1.y - p2.y)/(p1.x - p2.x)
        self.yintercept = p1.y - self.slope * p1.x
        self.epsilon = 0.00001

    def intersect(self, line2):
        if self.slope - line2.slope <= self.epsilon:
            if self.yintercept - line2.yintercept <= self.epsilon:
                return True
            else:
                return False
        print('here')
        return True
    def __repr__(self):
        klass = self.__class__
        return '%s(slope=%r, yintercept=%r)' % (klass, self.slope, self.yintercept)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

import pytest
@pytest.mark.parametrize('l1, l2, expected', [
    (Line(Point(2,5), Point(1,3)), Line(Point(-1, -1), Point(-2, -3)), True),
    (Line(Point(2,5), Point(1,3)), Line(Point(2, 4), Point(1, 3)), True),
    (Line(Point(10, 15), Point(40, 30)), Line(Point(15, 8), Point(49, 25)), False)
])
def test_sol(l1, l2, expected):
    assert l1.intersect(l2) == expected
