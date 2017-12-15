class Solution:
    def estimation(self, sol, guess):
        colors = 'rygb'
        if len(sol) != len(guess):
            return None
        hit, pseudo, frequency = 0, 0, {}
        for i in range(len(sol)):
            if sol[i] == guess[i]:
                hit += 1
            else:
                frequency[sol[i]] = frequency.get(sol[i], 0) + 1

        for i in range(len(guess)):
            if guess[i] != sol[i]:
                if guess[i] in colors and frequency.get(guess[i], 0) > 0:
                    frequency[guess[i]] -= 1
                    pseudo += 1
        return (hit, pseudo)

import pytest
@pytest.mark.parametrize('s, guess, expected', [
    ('rrgbb', 'rrrr', None),
    ('rggg', 'ybbb', (0, 0)),
    ('rrgr', 'rrrr', (3, 0)),
    ('rgby', 'ggrr', (1, 1))
])
def test_sol(s, guess, expected):
    sol = Solution()
    assert sol.estimation(s, guess) == expected
