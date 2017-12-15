def compressedSize(s):
    if len(s) == 0:
        return 0
    last = s[0]
    count, c = 0, 1
    for i in range(1, len(s)):
        if last == s[i]:
            c += 1
        else:
            count = count + 1 + len(str(c))
            last = s[i]
    return count + 1 + len(str(c))

def test_compressedSize():
    assert compressedSize('aaaaaa') == 2
    assert compressedSize('abcd') == 8
    assert compressedSize('abcdddddddddddddddddddddd') == 9


def compress(s):
    if len(s) < compressedSize(s):
        return s
    if len(s) == 0:
        return s
    compressed, count, last = [], 1, s[0]
    for i in range(1, len(s)):
        if s[i] == last:
            count += 1
        else:
            compressed.append(last)
            compressed.append(str(count))
            last = s[i]
            count = 1
    compressed.append(last)
    compressed.append(str(count))
    return ''.join(compressed)

def test_compressed():
    assert compress('') == ''
    assert compress('abcd') == 'abcd'
    assert compress('abcddddddddddd') == 'a1b1c1d11'
