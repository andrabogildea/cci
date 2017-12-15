def firstKthMagicNr(k):
    if k <= 0:
        return []
    index = {3:0, 5:0, 7:0}
    ct, l = 1, [1]
    while ct < k:
        next = 99999999
        for key,v in index.items():
            next = min(next, key * l[v])
        for key, v in index.items():
            if key * l[v] == next:
                index[key] += 1
        l.append(next)
        ct += 1
        print(ct,k)
    return l

import pytest
@pytest.mark.parametrize('input, expected', [
    (0, []),
    (1, [1]),
    (10, [1,3,5,7,9,15,21,25,27,35]),
    (13, [1,3,5,7,9,15,21,25,27,35,45,49,63])
])
def test_sol(input, expected):
    assert firstKthMagicNr(input) == expected
