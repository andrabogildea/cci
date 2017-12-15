def getBit(nr, bit):
    return nr & (1 << bit)

def find_missing(l, bit=None):
    if bit is None:
        bit = 0
    if bit > 7:
        return 0
    ones, zeroes = [], []
    for nr in l:
        if getBit(nr, bit) == 0:
            zeroes.append(nr)
        else:
            ones.append(nr)
    if len(zeroes) <= len(ones):
        res = find_missing(zeroes, bit+1)
        return (res << 1) | 0
    else:
        res = find_missing(ones, bit+1)
        return (res << 1) | 1

import pytest
@pytest.mark.parametrize('input, expected', [
    ([0,1,2,3,5,6,7,8,9,10,11,12,13], 4),
    ([0,1,2,3,4,5,6,7,9,10,11,12], 8)
])
def test_sol(input, expected):
    assert find_missing(input) == expected
