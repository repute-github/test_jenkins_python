#! /usr/bin/env python


"""This module does blah blah."""


# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print "And the output is -> ", [x for x in fibon(10)]
