"""This module does blah blah."""
#! /usr/bin/env python




# generator version
def fibon(total):
    """This function does blah blah."""
    first = second = 1
    for i in range(total):
        yield first
        first, second, i = second, first + second, i

print "And the output is -> ", [x for x in fibon(10)]

