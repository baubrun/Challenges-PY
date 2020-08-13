"""
Switching Between Pencils
When coloring a striped pattern, you may start by coloring each square sequentially,
 meaning you spend time needing to switch coloring pencils.

Create a function where given a list of colors cols, 
return how long it takes to color the whole pattern. Note the following times:

It takes 1 second to switch between pencils.
It takes 2 seconds to color a square.
See the example below for clarification.

color_pattern_times(["Red", "Blue", "Red", "Blue", "Red"]) ➞ 14

# There are 5 colors so it takes 2 seconds to color each one (2 x 5 = 10).
# You need to switch the pencils 4 times and it takes 1 second to switch (1 x 4 = 4).
# 10 + 4 = 14
Examples
color_pattern_times(["Blue"]) ➞ 2

color_pattern_times(["Red", "Yellow", "Green", "Blue"]) ➞ 11

color_pattern_times(["Blue", "Blue", "Blue", "Red", "Red", "Red"]) ➞ 13
Notes
Only change coloring pencils if the next color is different to the color before it.
Return a number in seconds.
"""

def color_pattern_times(cols):
    num_pencils = 0
    num_colors = len(cols)
    seconds = 0
    if num_colors == 1:
        return 2
    for c in range(len(cols) - 1):
        if cols[c] != cols[c + 1]:
            num_pencils += 1

    seconds = num_pencils + (num_colors * 2)
    return seconds



