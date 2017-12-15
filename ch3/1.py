# static implementatio
stack_size = 20
stack_top = [-1, -1, -1]
arr = [None] * stack_size * len(stack_top)

def push(stack, val):
    if is_full(stack):
        raise Exception('Out of memory,')
    stack_top[stack-1] += 1
    arr[(stack-1) * stack_size + stack_top[stack-1]] = val

def pop(stack):
    if is_empty(stack):
        raise Exception('Empty stack.')
    val = arr[(stack-1) * stack_size + stack_top[stack-1]]
    stack_top[stack-1] -= 1
    return val

def peek(stack):
    return arr[(stack-1) * stack_size + stack_top[stack-1]]

def is_empty(stack):
    return stack_top[stack-1] == -1

def is_full(stack):
    return stack_top[stack-1] + 1 >= stack_size

import pytest

def test_pop_empty():
    with pytest.raises(Exception) as excinfo:
        pop(0)
    assert 'Empty' in str(excinfo.value)

def test_push():
    for i in range(stack_size):
        push(2, i)
    assert peek(2) == i
    with pytest.raises(Exception) as excinfo:
        push(2, 2)
    assert 'Out' in str(excinfo.value)

def test_pop():
    assert pop(2) == 19

def test_push_stack3():
    for i in range(stack_size):
        push(3, i)
    assert peek(3) == i
    with pytest.raises(Exception) as excinfo:
        push(3, 2)
    assert 'Out' in str(excinfo.value)

def test_pop_stack3():
    for i in range(stack_size):
        pop(3)
    assert is_empty(3) == True
