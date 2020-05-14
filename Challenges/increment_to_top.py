"""
Create  a function that returns the total number of steps 
it takes to transform each element to the maximal element in the array. 
Each step consists of incrementing a digit by one.

Examples
increment_to_top([3, 4, 5]) ➞ 3
// 3 increments: 3 -> 4, 4 -> 5; 4 -> 5

increment_to_top([4, 3, 4]) ➞ 1

increment_to_top([3, 3, 3]) ➞ 0

increment_to_top([3, 10, 3]) ➞ 14
Notes
If the array contains only the Same digits, return 0 (see example #2).

Bonus: Can you write a solution that achieves 
this by only traversing the array once? 
(i.e. without finding the max before hand)
"""

def increment_to_top(arr):
    s = 0
    for i in arr: 
        s += max(arr) - i
    return s

print(increment_to_top([3, 4, 5]))
print(increment_to_top([4, 3, 4]))
print(increment_to_top([3, 3, 3]))
print(increment_to_top([3, 10, 3]))