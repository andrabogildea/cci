class Solution:
    def findSequence(self, l):
        if len(l) == 0:
            return (-1, -1)

        start = self.findStartUnsortedSequence(l)
        # the list is sorted
        if start == -1:
            return (-1, -1)
        end = self.findEndUnsortedSequence(l)
        min, max = self.findMinMax(l, start, end)
        # already sorted
        if min is None and max is None:
            return (-1, -1)
        start = self.expandLeft(l, start, min)
        end = self.expandRight(l, end, max)
        return (start, end)

    def expandLeft(self, l, start, min):
        new_start = start
        for i in range(start-1, -1, -1):
            if l[i] > min:
                new_start = i
        return new_start

    def expandRight(self, l, end, max):
        new_end = end
        for i in range(end+1, len(l)):
            if l[i] < max:
                new_end = i
        return new_end

    def findMinMax(self, l, start, end):
        min, max = None, None
        for i in range(start, end+1):
            if min is None or min > l[i]:
                min = l[i]
            if max is None or max < l[i]:
                max = l[i]
        return (min, max)

    def findStartUnsortedSequence(self, l):
        for i in range(1, len(l)):
            if l[i-1] > l[i]:
                return i - 1
        return len(l) - 1

    def findEndUnsortedSequence(self, l):
        end = -1
        for i in range(len(l)-2, -1, -1):
            if l[i] > l[i+1]:
                return i + 1
        return 0

import pytest
@pytest.mark.parametrize('l, expected', [
    ([], (-1, -1)),
    ([-1,2,3,4,5,6], (-1, -1)),
    ([6,5,4,3,2,1], (0, 5)),
    ([1,2,4,8,7,9,11,12], (3,4)),
    ([4,3,1,7,8,9], (0, 2)),
    ([1,2,3,4,9,7,6], (4, 6))
])
def test_findUnsortedSequence(l, expected):
    sol = Solution()
    assert sol.findSequence(l) == expected
