#!/usr/bin/env python3

# exersise 2-1

def do_twice(func):
    func()
    func()

def print_spam():
    print("spam")

do_twice(print_spam)
