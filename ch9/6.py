class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.sol(n,n,'', res)
        return res

    def sol(self, l, r, s, res):
        if l == 0 and r == 0:
            res.append(s)
        if l > 0:
            self.sol(l-1, r, s+'(', res)
        if r > l:
            self.sol(l, r-1, s+')', res)


import pytest
@pytest.mark.parametrize('n, expected', [
    (0, []),
    (1, ['()']),
    (2, ['()()', '(())']),
    (3, ['()()()', '(())()', '()(())', '((()))', '(()())'])
])
def test_sol(n, expected):
    sol = Solution()
    s = sol.generateParenthesis(n)
    assert len(s) == len(expected)
    for w in s:
        assert w in expected

