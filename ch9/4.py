from copy import copy
def subsets(s):
    if len(s) == 0:
        return []
    return subs(s, 0)

def subs(s, start):
    if start >= len(s):
        return [set()]
    l = [{s[start]}]
    tmp = subs(s, start+1)
    for subset in tmp:
        aux = copy(subset)
        aux.add(s[start])
        l.append(aux)
        l.append(subset)
    return l

import pytest
@pytest.mark.parametrize('s, expected', [
    ([], []),
    ([0], [set(), {0}]),
    ([0, 1], [set(), {0}, {1}, {0, 1}]),
    ([0,1,2], [set(), {0}, {1}, {2}, {0,1}, {0,2}, {0,1,2}, {1,2}])
])
def test_sol(s, expected):
    for s in subsets(s):
        assert s in expected
