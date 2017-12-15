# 4kb <= 4000 bytes <= 32.000 bytes
# 4kb > 32.000 bytes >= 2**15 but
# 2**15 <= 4kb
class BitSet:
    def __init__(self, size):
        self.bitvector = bytearray([0] * (size >> 3))

    def __setitem__(self, key, value):
        self.bitvector[(key >> 3)] |= (1 << (key % 8))

    def __getitem__(self, key):
        bit = (self.bitvector[key >> 3] & (1 << (key % 8)))
        if bit == 0:
            return 0
        return 1

class Solution:
    def solution(self, l):
        res = []
        bitvector = BitSet(32000)
        for el in l:
            if bitvector[el] == 1:
                res.append(el)
            else:
                bitvector[el] = 1
        return res

import pytest
@pytest.mark.parametrize('input, expected', [
    ([1,2,3,4,7,5,6,7,8,9,10,1,2], [7,1,2]),
    ([], []),
    ([1,2,3,4,5,6], [])
])
def test_solution(input, expected):
    sol = Solution()
    assert sol.solution(input) == expected

