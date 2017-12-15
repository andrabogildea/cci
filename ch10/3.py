class Solution:
    def generateNew(self, fd):
        bitvector = bytearray([0] * (int(2**31 / 8)))
        nr = fd.readline()
        while nr != '':
            number = int(nr.strip('\n'))
            # put the index in reverse order in a bit because is easier to compute
            bitvector[int(number/8)] |= 1 << (number % 8)
            nr = fd.readline()
        for i, nr in enumerate(bitvector):
            if nr < 255:
                for j in range(8):
                    if nr & (1 << j) == 0:
                        return i * 8 + j
        return None

    def generateNew2(self, fd):
        rangeSize = 2**20 # has to be between 2**10 and 2**26
        arraySize = int(2**31/rangeSize)
        blocks = [0] * arraySize
        bitvector = bytearray([0] * int(rangeSize/8))

        nr = fd.readline()
        while nr != '':
            number = int(nr.strip('\n'))
            blocks[int(number/rangeSize)] += 1
            nr = fd.readline()
        missingStart = -1
        for i in range(arraySize):
            if blocks[i] < rangeSize:
                missingStart = i * rangeSize
                break

        fd.seek(0)
        nr = fd.readline()
        while nr != '':
            number = int(nr.strip('\n'))
            # put the index in reverse order in a bit because is easier to compute
            if number >= missingStart and number <= missingStart + rangeSize:
                bitvector[int((number-missingStart)/8)] |= 1 << ((number - missingStart) % 8)
            nr = fd.readline()
        for i, nr in enumerate(bitvector):
            if nr < 255:
                for j in range(8):
                    if nr & (1 << j) == 0:
                        return i * 8 + j
        return None

import pytest
@pytest.mark.parametrize('file_name, expected', [
    ('./test3.txt', 4)
])
def test_sol(file_name, expected):
    sol = Solution()
    with open(file_name, 'r') as fd:
        assert sol.generateNew(fd) == expected
        fd.seek(0)
        assert sol.generateNew2(fd) == expected
