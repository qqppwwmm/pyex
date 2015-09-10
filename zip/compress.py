def compress(list):
    b = 0
    c = []

    for x in list:
        if x == 'x':
            c.append(b)
        b = b + 1
    return c
