"""
Find the Largest Even Number
Write a function that finds the largest number 
in an array nums that is also even. 
If there is no even number, return -1.

Examples
largestEven([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10

largestEven([1, 3, 5, 7]) ➞ -1

largestEven([0, 19, 18973623]) ➞ 0
"""


def largest_even(nums):
    largest = 0
    evens = 0
    for i in nums:
        if i % 2 == 0:
            evens += 1
            largest = max(i, largest)
    if evens > 0:
        return largest
    return -1


