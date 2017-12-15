def is_substring(str, substr):
    return substr in str

def is_rotation(s1, s2):
    return is_substring(s1+s1, s2)

def test_is_rotation():
    assert is_rotation('abbaababbaaaaab', 'bbaaaaababbaaba') == True
    assert is_rotation('abcdab', 'cdabab') == True
    assert is_rotation('abcdefg', 'aefgbcd') == False
