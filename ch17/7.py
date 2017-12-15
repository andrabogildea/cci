class Solution:
    def __init__(self):
        self.digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seve', 'eight', 'nine']
        self.tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        self.teens = ['eleven', 'tweleve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        self.order = ['', 'thousand', 'million']

    def numToString(self, nr):
        if nr > 999999999:
            return None
        if nr == 0:
            return 'zero'

        if nr < 0:
            return 'Negative ' + self.numToString(-1*nr)

        ord, sol = 0, ''
        while nr > 0:
            if nr % 1000 > 0:
                sol = self.numHundredToString(nr % 1000)+ self.order[ord] + ' ' + sol
                nr = int(nr/1000)
                ord += 1
        return sol.strip()

    def numHundredToString(self, nr):
        s = ''

        if nr > 99:
            s += self.digits[int(nr/100) - 1] + ' hundred '
            nr = nr % 100

        if nr == 10 or nr > 19:
            s += self.tens[int(nr/10) - 1] + ' '
            nr = nr % 10
        elif nr > 10 and nr < 20:
            s += self.teens[nr - 11] + ' '
            nr = 0

        if nr > 0 and nr < 10:
            s += self.digits[nr - 1] + ' '

        return s

import pytest
@pytest.mark.parametrize('nr, expected', [
    (0, 'zero'),
    (10, 'ten'),
    (12, 'tweleve'),
    (20, 'twenty'),
    (32, 'thirty two'),
    (500, 'five hundred'),
    (901, 'nine hundred one'),
    (-6382, 'Negative six thousand three hundred eighty two'),
    (123405, 'one hundred twenty three thousand four hundred five'),
    (1234069, 'one million two hundred thirty four thousand sixty nine')
])
def test_sol(nr, expected):
    sol = Solution()
    assert sol.numToString(nr) == expected
