#!/usr/bin/env python3

# exersise 2-3
# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

# intentionally not using variables

# the total miles
# 10 / 1.61
# >>  6.211
print(10 / 1.61)

# the average pace

# the total seconds
# 42 * 60 + 42
# >> 2562
print(40 * 60 + 42)

# the pace in seconds per mile
# 2562 / 6.211
# >> 412.494
print(2562 / 6.211)

# the amount of minutes in 412.494 seconds
# 412.494 / 60
# >> 6.874
# this is 6 minutes and a 0.874 minutes worth of seconds
print(412.494 / 60)

# OR using integer division
# 412.494 // 60
# >> 6.0
print(412.494 // 60)

# the remaining seconds
# 412.494 - (6 * 60)
# >> 52.494
print(412.494 - (6 * 60))

# OR using modulus 
# 412 % 60
# >> 52.494
print(412 % 60)

# the average pace is 6 minutes and 52.494 seconds per mile
# 6:52 per mile

# What is your average speed in miles per hour?

# if the average pace is 6 minutes and 52.494 seconds per miles, or 6.874 minutes per mile
# 60 minutes ( 1 hour ) will accomedate for 60 minutes * ( 1 mile / 6.874 minutes )
# 60 / 6.874
# >> 8.727
print(60 / 6.874)

# the average pace is 8.272 miles per hour
