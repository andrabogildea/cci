from collections import deque


class Solution:
    def existsPath(self, graph, start, target):
        visited = set()
        to_visit = deque([start])
        while len(to_visit) > 0:
            current = to_visit.popleft()
            while current in visited:
                if len(to_visit) <= 0:
                    return False
                current = to_visit.popleft()
            if current == target:
                return True
            neighbours = graph.get(current, [])
            for neighbour in neighbours:
                to_visit.append(neighbour)
            visited.add(current)
        return False

# ---------------Tests----------------------
import pytest

@pytest.mark.parametrize('graph, start, target, expected', [
    ({}, 1, 2, False),
    ({1:[2,3], 2:[1,3], 3:[5], 4:[4,5]}, 1, 5, True),
    ({1:[1,2], 2:[3], 3:[1], 4:[3,5], 5:[3,4]}, 1, 5, False)
])
def test_existsPath(graph, start, target, expected):
    sol = Solution()
    assert sol.existsPath(graph, start, target) == expected
