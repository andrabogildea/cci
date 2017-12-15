solution(s):
    # use 57 so I do not have to exclude chr between Z and a
    if len(s) > 57:
        return False
    visited = [False] * 57
    for chr in s:
        print(ord(chr) - ord('A'))
        if visited[ord(chr) - ord('A')]:
            return False
        visited[ord(chr) - ord('A')] = True
    return True

def solution2(s):
    # without data structurse - sorting
    s = list(s)
    s.sort()
    s = ''.join(s)
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            return False
    return True


def solution3(s):
    # without data structures - bitmap
    check = 0
    for chr in s:
        val = ord(chr) - ord('A')
        if (1 << val) & check != 0:
            return False
        check |= 1 << val
    return True

import pytest
@pytest.mark.parametrize("test_input,expected", [
    ('', True),
    ('abcdef', True),
    ('abceta', False),
    ('bbbb', False)
])
def test_solutions(test_input, expected):
    assert solution(test_input) == expected
    assert solution2(test_input) == expected
    assert solution3(test_input) == expected
