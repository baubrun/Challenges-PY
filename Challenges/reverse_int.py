"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.

"""



def reverse(x):
    remainder = 0
    rev = 0
    while x != 0:
        remainder = x % 10
        x //= 10
        rev = (rev * 10) + remainder
    return rev


print(reverse(123))
print(reverse(-123))
print(reverse(120))
