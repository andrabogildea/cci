class Box:
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    def __gt__(self, other):
        return self.w > other.w and self.h > other.h and self.d > other.d

    def __lt__(self, other):
        return self.w < other.w and self.h < other.h and self.d < other.d

    # def __eq__(self, other):
    #     return self.w == other.w and self.h == other.h and self.d == other.d

    def canBeAbove(self, other):
        if other is None:
            return True
        return self < other

class Solution:
    def findBigestStack(self, boxes):
        if len(boxes) == 0:
            return []
        return self.bigestStack(boxes, None)

    def bigestStack(self, boxes, prev_box, cache=None):
        if cache is None:
            cache = {}
        if prev_box in cache:
           return cache[prev_box]
        max_height, max_stack = -1, []
        for box in boxes:
            if box.canBeAbove(prev_box):
                stack = self.bigestStack(boxes, box)
                if self.stackHeigth(stack) > max_height:
                    max_height = self.stackHeigth(stack)
                    max_stack = stack
        if prev_box is not None:
            max_stack.insert(0, prev_box)
        cache[prev_box] = max_stack
        return max_stack

    def stackHeigth(self, stack):
        s = 0
        for box in stack:
            s += box.h
        return s

def test_solution():
    b1 = Box(5,10,3)
    b2 = Box(5,7,3)
    b3 = Box(4,8,2)
    b4 = Box(3,3,1)
    boxes = [b1, b2, b3, b4]
    sol = Solution().findBigestStack(boxes)
    expected = [b1, b3, b4]
    for box in sol:
        assert (box in expected) == True
    for box in expected:
        assert (box in sol) == True
