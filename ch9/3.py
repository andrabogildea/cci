def findMagicIndex(a):
    l, r = 0, len(a) - 1
    return findIndex(a, l, r)

def findIndex(a,l,r):
    if l > r:
        return -1
    mid = int((l + r) / 2)
    if a[mid] == mid:
        return mid
    if a[mid] > mid:
        return findIndex(a, l, mid-1)
    return findIndex(a, mid+1, r)


def findMagicIndex2(a):
    l, r = 0, len(a) - 1
    return findIndex2(a, l, r)

def findIndex2(a, l, r):
    if l > r:
        return -1
    mid = int((l + r) / 2)
    if a[mid] == mid:
        return mid
    # search left
    r2 = min(a[mid], mid-1)
    index = findIndex2(a, l, r2)
    if index > -1:
        return index
    l2 = max(a[mid], mid+1)
    return findIndex2(a, l2, r)

import pytest
@pytest.mark.parametrize('arr, expected', [
    ([], -1),
    ([0], 0),
    ([-1, 4, 6], -1),
    ([-10, -1, 2, 4, 6, 8], 2),
    ([-10, 1, 3, 5, 6 ,9], 1),
    ([-11, 0, 1, 3], 3),
    ([-11, 0, 2, 8], 2),
    ([0, 4 ,5, 6 ,7], 0)
])
def test_findMagicIndex(arr, expected):
    assert findMagicIndex(arr) == expected


@pytest.mark.parametrize('arr, expected', [
    ([], -1),
    ([-1,2,3,3,3,5,6,9], 3),
    ([-1, 2, 6, 6, 7,7,7, 7], 7),
    ([0, 3, 3, 4 ,6,7,8], 0)
])
def test_sol(arr, expected):
    assert findMagicIndex2(arr) == expected
