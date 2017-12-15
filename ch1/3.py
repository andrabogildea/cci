def sol(s1, s2):
    s1, s2 = list(s1), list(s2)
    s1.sort()
    s2.sort()
    s1 = ''.join(s1)
    s2 = ''.join(s2)
    return s1 == s2

def sol2(s1, s2):
    if len(s1) != len(s2):
        return False
    ct = {}
    for chr in s1:
        ct[chr] = ct.get(chr, 0) + 1
    for chr in s2:
        ct[chr] = ct.get(chr, 0) - 1
        if ch[chr] < 0:
            return False
    return True

import pytest
@pytest.mark.parametrize('input,expected', [
    (('abcdefa', 'cfbdeaa'), True),
    (('', ''), True),
    (('bbbba', 'bbbbbb'), False),
    (('bbbbbbb', 'bb'), False)
])
def test_sol(input, expected):
    print(input)
    print(expected)
    assert sol(input[0], input[1]) == expected
    assert sol(input[0], input[1]) == expected
