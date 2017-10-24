#! /usr/bin/env python

# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print [x for x in fibon(10)]