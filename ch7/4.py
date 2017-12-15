def multiply(a, b):
    if abs(a) < abs(b):
        return multiply(b, a)
    nr = 0
    for i in range(abs(b)):
        nr += a
    if b < 0:
        return negate(nr)
    return nr

def negate(nr):
    n = 1
    if nr > 0:
        n = -1
    neg = 0
    for i in range(abs(nr)):
        neg += n
    return neg

def subtract(a, b):
    return a + negate(b)

def divide(a, b):
    if b == 0:
        return None
    absa, absb = abs(a), abs(b)
    prod, ct = 0, 0
    while prod + absb <= absa:
        prod += absb
        ct += 1
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return ct
    return negate(ct)

def test_divide():
    assert divide(1, 0) == None
    assert divide(4, 10) == 0
    assert divide(5, 5) == 1
    assert divide(21, 5) == 4
    assert divide(21, -5) == -4
    assert divide(-6, -3) == 2

def test_negate():
    assert negate(0) == 0
    assert negate(-1) ==1
    assert negate(1) == -1

def test_multiply():
    assert multiply(2, 0) == 0
    assert multiply(2, 4) == 8
    assert multiply(-3, 9) == -27
    assert multiply(-9, -2) == 18

def test_subtract():
    assert subtract(5, 7) == -2
    assert subtract(12, 3) == 9
    assert subtract(-5, 7) == -12
    assert subtract(13, -20) == 33
    assert subtract(-21, -22) == 1

