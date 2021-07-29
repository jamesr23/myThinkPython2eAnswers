#!/usr/bin/env python3

# exersise 2-2
def do_twice(func, arg):
    func(arg)
    func(arg)

do_twice(print, "spam")
