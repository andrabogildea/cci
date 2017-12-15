def merge(n, m, j, i):
    # n = 10000000000
    # m =       10011
    # j = 6, i = 2
    # merged = 10001001100

    # clear bits betwee i and j inclusive
    # first make all ones befor j and the rest 11110000000
    ones = ~0
    left = ones << (j + 1)

    # make ones after i 00000000011
    right = (1 << i) - 1

    # merge left and right to obtaint the maks
    mask = left | right

    # clear bits in n
    n_cleared = n & mask

    # shift m
    m_shifted = m << i

    #merge m in n
    merged = n_cleared | m_shifted
    return merged

import pytest
@pytest.mark.parametrize('n,m,j,i,expected', [
    (0b10000000000, 0b10011, 6, 2, 0b10001001100)
])
def test_merge(n,m,j,i,expected):
    assert merge(n,m,j,i) == expected
