def getNext(nr):
    # find right most 0 that has trailing ones and count ones and zeroes after it
    if nr == 0:
        return -1
    n = nr
    ct0 = 0
    while n & 1 == 0 and n > 0:
        ct0 += 1
        n = n >> 1
    ct1 = 0
    while n & 1 == 1:
        ct1 += 1
        n = n >>1
    if ct1 + ct0 == len(bin(nr))-2:
        return -1

    pos = ct1 + ct0

    # switch bite on pos to 1
    nr = nr | (1 << pos)
    # zero everything after p
    nr = nr & (~0 << pos)
    # put ct1 ones the right
    nr = nr | ((1 << (ct1-1)) - 1)
    return nr

def getPrev(nr):
    # oposite to next
    # Find rightmost one that has trailing zeroes and count ones and zeroes after it

    if nr == 0:
        return -1
    ct1 = 0
    n = nr
    while n & 1 == 1:
        ct1 += 1
        n >>= 1
    ct0 = 0
    while n & 1 == 0 and n != 0:
        ct0 += 1
        n >>= 1
    if ct0 == 0:
        return -1
    # switch pos byte to 0 and 0 everything after
    pos = ct0 + ct1
    nr = nr & (~0 << (pos+1))
    # add ct1 + 1 ones after pos
    ones = (1 << (ct1+1)) - 1
    ones <<= (ct0 - 1)
    nr |= ones
    return nr



import pytest
@pytest.mark.parametrize('input, next, prev', [
    (0b11011001111100, 0b11011010001111, 0b11011001111010),
    (0b1000000000, -1, 0b0100000000),
    (0b1111000000, -1, 0b1110100000),
    (0b1111101111, 0b1111110111, 0b1111011111),
    (0b1111111111, -1, -1)
])
def test(input, next,prev):
    assert getNext(input) == next
    assert getPrev(input) == prev
