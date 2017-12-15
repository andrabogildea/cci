def rotate(m):
    # create new matrix
    if len(m) == 0:
        return []
    rotated = []
    nrc, nrr = len(m[0]), len(m)
    for col in range(nrc):
        new_line = []
        for line in range(nrr-1, -1, -1):
            new_line.append(m[line][col])
        rotated.append(new_line)
    return rotated

def rotate2(m):
    size = len(m)
    for layer in range(int(size/2)):
        end = size - layer - 1
        for i in range(layer, end):
            right = m[i][end]
            # top -> right
            m[i][end] = m[layer][i]
            # left -> top
            m[layer][i] = m[end-i+layer][layer]
            # bottom -> left
            m[end-i+layer][layer] = m[end][end-i+layer]
            # right -> bottm
            m[end][end-i+layer] = right
    return m


import pytest
@pytest.mark.parametrize('input,expected', [
    ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
    ([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], [[13,9,5,1], [14,10,6,2], [15,11,7,3], [16, 12, 8, 4]])
])
def test(input, expected):
    assert rotate(input) == expected
    assert rotate2(input) == expected
