class Solution:
    def solution(self, people):
        # people.sort()
        tail = [1] * len(people)
        maxsize = -1
        for i in range(1, len(people)):
            for j in range(i-1, -1, -1):
                print(i, j)
                if people[j] < people[i]:
                    tail[i] += tail[j]
                    if tail[i] > maxsize:
                        maxsize = tail[i]
                    break
        return maxsize

import pytest
@pytest.mark.parametrize('people, expected', [
    ([13, 14, 10, 11, 12], 3)
])
def test_solution(people, expected):
    sol = Solution()
    assert sol.solution(people) == expected
