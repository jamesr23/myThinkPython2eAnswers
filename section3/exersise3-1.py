#!/usr/bin/env python3

# exersise 3-1

def draw_row(prefix, content, amount):
    # row = '+' + '-' * 4
    row = prefix + (content * 4)
    # +---
    print(row * amount, end = '')
    print(prefix)

def print_grid():
    draw_row('+', '-', 2)
    draw_row('|', ' ', 2)
    draw_row('|', ' ', 2)
    draw_row('|', ' ', 2)
    draw_row('+', '-', 2)
    draw_row('|', ' ', 2)
    draw_row('|', ' ', 2)
    draw_row('|', ' ', 2)
    draw_row('+', '-', 2)

print_grid()

"""
this could be made shorter by using do_twice;
however without being able to pass in lists / list expantion,
there would have to be do_twice_3arg(func, arg1, arg2, arg3)
and its not hundreds of times, personally i think this is fine.

"""
