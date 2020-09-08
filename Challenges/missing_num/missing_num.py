"""
Create a function that takes an array of 
numbers between 1 and 10 (excluding one number) and returns the missing number.

Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
Notes
The array of numbers will be unsorted (not in order).
Only one number will be missing.

"""

def missing_num(lst):
    l = sorted(lst)
    ans = 0
    for i in range(len(l)):
        if (l[i] != i + 1):
            ans = i + 1
            break
    return 10 if ans is 0 else ans

