#!/usr/bin/env python3

# exersise 3-2

"""
prefix: the thing to print at the edge of the row
content: the string to repeat in the middle
amount: the amount of times to print the row before ending it
"""
# compile the row string
# row = (edge + (content * 4)) * amount + edge # <- a bit confusing to look at.
# the best code is the mos readable :D
def print_row(edge, content, amount):
    # row = "+----", "|     "
    row = edge + (content * 4)
    
    # print it amount times
    print(row * amount, end = '')
    
    # print the edge character finally
    print(edge)

# this is the same thing, but messier
def print_row_unreadable(edge, content, amount):
    print((edge + (content * 4)) * amount + edge)


"""
square_amount: the amount of squares to print horozontally
"""
def print_squares(square_amount):
    print_row('+', '-', square_amount)
    print_row('|', ' ', square_amount)
    print_row('|', ' ', square_amount)
    print_row('|', ' ', square_amount)

def print_grid():
    print_squares(3)
    print_squares(3)
    print_squares(3)
    print_row('+', '-', 3)

print_grid()

"""
this was fun, i think it'l be more fun once returning values, repetition, and data structures are avaliable :)

firstly, i created the function print_row.
it takes in the edges and creates (and prints) a row that repeats over $amount times

then, print_squares uses print_row to print the $square_amount of squares ( without a bottom though! )

print_grid wraps it all up by calling the function that prints the squares, and finishing it up with the appropriate row ( with the row function! )

allens solution is also good considering the restrictions,
but personally i can just get lost in all the functions being passed into others, and again.
"""
