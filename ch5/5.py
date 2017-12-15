def diff_bits(a, b):
    c = a ^ b
    ct = 0
    while c != 0:
        if c & 1 == 1:
            ct += 1
        c >>= 1
    return ct

import pytest

@pytest.mark.parametrize('a, b, sol', [
    (0b0, 0b0, 0),
    (0b0, 0b1, 1),
    (0b1001001, 0b0110110, 7),
    (0b100101110, 0b100001100, 2),
    (0b10101010, 0b10101010, 0)
])
def test_sol(a, b, sol):
    assert diff_bits(a, b) == sol
