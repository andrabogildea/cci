class Solution:
    def searchWord(self, words, word):
        if len(word) == 0:
            return False
        return self.searchW(words, word, 0, len(words) - 1)

    def searchW(self, words, word, l, r):
        if l > r:
            return False
        mid = int((l + r) / 2)
        if words[mid] == '':
            left, right = mid - 1, mid + 1
            while True:
                if left < l and right > r:
                    return False
                if left >= l and words[left] != '':
                    mid = left
                    break
                if right <= r and words[right] != '':
                    mid = right
                    break
                left -= 1
                right += 1
        if words[mid] == word:
            return True
        if words[mid] > word:
            return self.searchW(words, word, l, mid - 1)
        else:
            return self.searchW(words, word, mid + 1, r)

import pytest
@pytest.mark.parametrize('words, word, expected', [
    ([], '', False),
    (['a', 'b', '','c', '', '', '', '', 'd', 'e'], 'a', True),
    (['a', 'b', '','c', '', '', '', '', 'd', 'e'], 'd', True),
    (['a', 'b', '','c', '', '', '', '', 'd', 'e'], 'x', False),
])
def test_sol(words, word, expected):
    sol = Solution()
    assert sol.searchWord(words, word) == expected
