def permutations(string):
    if len(string) == 0:
        return []
    return perm(string, 0)

def perm(string, start):
    if start >= len(string):
        return ['']
    sol = []
    words = perm(string, start+1)
    for word in words:
        for i in range(len(word) + 1):
            if i > 0 and len(word) > 0 and string[start] == word[i-1]:
                continue
            tmp = word[:i] + string[start] + word[i:]
            sol.append(tmp)
    return sol

import pytest
@pytest.mark.parametrize('string, expected', [
    ('', []),
    ('a', ['a']),
    ('ab', ['ab', 'ba']),
    ('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
    ('aba', ['aba', 'baa', 'aab'])
])
def test_permutations(string, expected):
    perms = permutations(string)
    for word in perms:
        assert word in expected
    for word in expected:
        assert word in perms
