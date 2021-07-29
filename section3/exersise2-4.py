#!/usr/bin/env python3

# exersise 2-4

def do_twice(func, arg):
    func(arg)
    func(arg)

def print_twice(s):
    print(s)
    print(s)

do_twice(print_twice, "spam")
