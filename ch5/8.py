def draw_line(screen, width, x1, x2, y):
    # find first full byte
    start_offset = x1 % 8
    first_full_byte = int(x1 / 8)
    if start_offset != 0:
        first_full_byte += 1

    end_offset = x2 % 8
    last_full_byte = int(x2 / 8)
    if end_offset < 7:
        last_full_byte -= 1

    # replace full bytes
    for byte in range(first_full_byte, last_full_byte + 1):
        screen[int(width / 8) * y + byte] = 0xff

    # creat masks
    start_mask = 0xff >> start_offset
    end_mask = ~0 << (7 - end_offset)

    # if start and end on same bit
    if x1 / 8 == x2 / 8:
        mask = start_mask & end_mask
        screen[int(width / 8) * y + int(x1 / 8)] |= mask
    else:
        if start_offset != 0:
            screen[int(width / 8) * y + int(x1 / 8)] |= start_mask
        if end_offset != 7:
            screen[int(width / 8) * y + int(x2 / 8)] |= end_mask
    return screen

import pytest
@pytest.mark.parametrize('screen, w, x1, x2, y, expected', [
    ([0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0], 7, 9, 30, 1, [0,0,0,0,0,0,0, 0,0b01111111,255,0b1111110,0,0,0, 0,0,0,0,0,0,0]),
    ([0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0], 7, 9, 10, 1, [0,0,0,0,0,0,0, 0,0b01100000,0,0,0,0,0, 0,0,0,0,0,0,0])
])
def test_sol(screen, w, x1, x2, y, expected):
    assert draw_line(screen, w, x1, x2, y)

