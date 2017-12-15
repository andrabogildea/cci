def sol(m):
    if len(m) == 0:
        return m
    rows, cols = len(m), len(m[0])
    zr, zc = 0, 0
    # scan matrix to see which r and coll have to be zeroed
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == 0:
                zr = zr | (1 << row)
                zc = zc | (1 << col)

    # scan the matrix and zero the rows and colls
    for row in range(rows):
        for col in range(cols):
            if ((1 << row) & zr !=0) or ((1 << col) & zc !=0):
                m[row][col] = 0
    return m


import pytest
@pytest.mark.parametrize('input,expected', [
    ([[1,0,1],[1,0,1],[0,1,1],[1,1,1]], [[0,0,0],[0,0,0],[0,0,0],[0,0,1]]),
    ([], [])
])
def test_sol(input,expected):
    assert sol(input) == expected
