#!/usr/bin/env python3

# exersise 2-5

def do_twice(func, arg):
    func(arg)
    func(arg)

def print_twice(s):
    print(s)
    print(s)

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_four(print, "spam")
