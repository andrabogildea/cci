def swap_bits(nr):
    return ((nr & 0xaaaaaaa) >> 1) | ((nr & 0x5555555) << 1)

import pytest
@pytest.mark.parametrize('input, expected', [
    (0b10, 0b01),
    (0b1, 0b10),
    (0b100110110, 0b1000111001),
    (0b10111010, 0b01110101)
])
def test_sol(input, expected):
    assert swap_bits(input) == expected
