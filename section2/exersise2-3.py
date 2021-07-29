#!/usr/bin/env python3

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?

initial_hour = 6
initial_minutes = 52

# or 8 + 15 / 60
easy_pace = 8.25

# or 7 + 12 / 60 (12 is 1 fifth)
other_pace = 7.2

# the time took for the trip
dminutes = (2 * easy_pace) + (3 * other_pace)

final_minutes = initial_minutes + dminutes

# in the book, we are supposed to be using the interpreter as a calculator, so you could figure out
final_minutes
# >> 90.1
# 90.1 minutes after 6am is 07:30

# to do this in "script mode" - fully automate it
hours = initial_hour # 6
minutes = final_minutes # 90.1
hours = hours + (minutes // 60) # 6 + 1
minutes = minutes % 60 # 90.1 - (90 // 6); the remainder if divided by 60

print("time(decimals):")
print(str(hours) + ":" + str(minutes))

# to make it look nicer (round down)
print("time(rounded):")
print(str(int(hours)) + ":" + str(int(minutes)))

# but there are many ways to do this,
# you could even convert it all to seconds
# and add them and convert them back
# i chose to work in minutes
# because there is less conversion to deal with that way

# by the way, if you wanted to do this in seconds...

initial_seconds = (60 * 60 * 6) + (60 * 52)

# the paces.. in seconds
easy_pace_seconds = (60 * 8) + 15
other_pace_seconds = (60 * 7) + 12

dseconds = easy_pace_seconds * 2 + other_pace_seconds * 3

final_seconds = initial_seconds + dseconds

seconds = final_seconds % 60
total_minutes = final_seconds // 60
minutes = total_minutes % 60
hours = total_minutes // 60

print("time(seconds):")
print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

# results will be slightly different due to integer division
