class Solution:
    def sortAnagrams(self, l):
        l.sort(key=lambda x: ''.join(sorted(x)))

    def sortAnagrams2(self, l):
        dict = {}
        for word in l:
            key = ''.join(sorted(word))
            dict.setdefault(key, []).append(word)
        i = 0
        for vals in dict.values():
            for val in vals:
                l[i] = val
def test_sol():
    pass
