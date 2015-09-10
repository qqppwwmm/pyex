# -*- coding: utf-8 -*-
def extract(xcoordinate, listlen):
    c = []
    for _ in range(listlen):
        for xx in xcoordinate:
            if xx == len(c):
                c.append('x')
        if len(c) < listlen:
            c.append(0)
    return c


PI = 3.14
