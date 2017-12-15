def solution(s):
    end = 0
    while end < len(s):
        if s[end] == '\n':
            break
        end += 1
    end -= 1
    start = 0
    s = list(s)
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)

def test_sol():
    assert solution('') == ''
    assert solution('abcd') == 'dcba'
    assert solution('a') == 'a'
    assert solution('a\n') == 'a\n'
    assert solution('abcd\n') == 'dcba\n'
    assert solution('abcd\n\n\n') == 'dcba\n\n\n'
