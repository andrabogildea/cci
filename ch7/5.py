class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_on_segment(self, segment):
        if min(segment.p1.x, segment.p2.x) <= self.x <= max(segment.p1.x, segment.p2.x)\
           and min(segment.p1.y, segment.p2.y) <= self.y <= max(segment.p1.y, segment.p2.y):
            return True
        return False

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Square:
    def __init__(self, leftx, rightx, bottomy, topy):
        self.leftx = leftx
        self.rightx = rightx
        self.bottmy = bottomy
        self.topy = topy

    def getMiddle(self):
        middlex = (self.rightx - self.leftx) / 2 + self.leftx
        middley = (self.topy - self.bottmy) / 2 + self.bottmy
        return Point(middlex, middley)

class Line:
    def __init__(self, p1, p2):
        # the line is vertical
        if p1.x - p2.x == 0:
            pass # do something else
        else:
            self.slope = (p1.y - p2.y) / (p1.x - p2.x)
        self.yintercept = p1.y - self.slope * p1.x
        self.epsilon = 0.000001

    def intersection_point_with_line(self, line2):
        numerator = line2.yintercep - self.yintercept
        denominator = self.solpe - line2.slope
        if denominator < self.epsilon:
            return None
        x = numerator / denominator
        y = self.epsilon * x + self.yintercept
        return Point(x, y)

    def __repr__(self):
        klass = self.__class__
        return '%s(slope=%r, yintercept=%r)' % (klass, self.slope, self.yintercept)
