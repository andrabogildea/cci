class Solution():
    def countWays(self, expression, res):
        if len(expression) == 0:
            return 0
        return self.count(expression, res, 0, len(expression)-1)

    def count(self, exp, result, s, e, cache=None):
        if cache is None:
            cache = {}
        if (s,e) in cache:
            return cache[(s, e)]
        if s == e:
            if exp[s] == '1' and result == True:
                return 1
            elif exp[s] == '0' and result == False:
                return 1
            else:
                return 0
        ct = 0
        for i in range(s+1, e, 2):
            if result == True:
                if exp[i] == '&':
                    ct += (self.count(exp, result, i+1, e, cache) * self.count(exp, result, s, i-1, cache))
                elif exp[i] == '|':
                    ct += (self.count(exp, result, i+1, e, cache) * self.count(exp, not result, s, i-1, cache)+\
                               self.count(exp, not result, i+1, e, cache) * self.count(exp, result, s, i-1, cache)+\
                               self.count(exp, result, i+1, e, cache) * self.count(exp, result, s, i-1, cache))
                elif exp[i] == '^':
                    ct += (self.count(exp, result, i+1, e, cache) * self.count(exp, not result, s, i-1, cache)+\
                               self.count(exp, not result, i+1, e, cache) * self.count(exp, result, s, i-1, cache))
            if result == False:
                if exp[i] == '&':
                    ct += (self.count(exp, result, i+1, e, cache) * self.count(exp, result, s, i-1, cache)+\
                               self.count(exp, result, i+1, e, cache) * self.count(exp, not result, s, i-1, cache)+\
                               self.count(exp, not result, i+1, e, cache) * self.count(exp, result, s, i -1))
                elif exp[i] == '|':
                    ct += (self.count(exp, result, i+1, e, cache) * self.count(exp, result, s, i-1, cache))
                elif exp[i] == '^':
                    ct += (self.count(exp, result, i+1, e, cache) * self.count(exp, result, s, i-1, cache)+\
                               self.count(exp, not result, i+1, e, cache) * self.count(exp, not result, s, i-1, cache))
        cache[(s, e)] = ct
        return ct

import pytest
@pytest.mark.parametrize('expr, res, expected', [
    ('1&1', True, 1),
    ('1&11', False, 0),
])
def test_sol(expr, res, expected):
    s = Solution()
    assert s.countWays(expr, res) == expected
