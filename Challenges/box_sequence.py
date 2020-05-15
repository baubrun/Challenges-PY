"""
Create a function that takes a number (step) as an argument
and returns the amount of boxes in that step of the sequence.

Box Sequence Image

Step 0: Start with 0
Step 1: Add 3
Step 2: Subtract 1
Repeat Step 1 & 2 ...

Examples
box_seq(0) ➞ 0

box_seq(1) ➞ 3

box_seq(2) ➞ 2
Notes
Step (the input) is always a positive integer (or zero).
"""


def box_seq(step):
    s = 0
    if step == 0:
        return 0
    for i in range(1, step + 1):
        if i % 2 == 1:
            s += 3
        elif i % 2 == 0:
            s -= 1
    return s

print(box_seq(0))
print(box_seq(1))
print(box_seq(2))
print(box_seq(6))
