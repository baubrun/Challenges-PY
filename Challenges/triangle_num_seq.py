"""
Triangular Number Sequence
This Triangular Number Sequence is generated from 
a pattern of dots that form a triangle. 
The first 5 numbers of the sequence, or dots, are: 1, 3, 6, 10, 15. 
Write a function that converts n number of places with its corresponding number.

Examples
triangle(1) ➞ 1

triangle(6) ➞ 21

triangle(215) ➞ 23220
"""




def triangle(n):
    s = 0
    for i in range(1, n + 1):
         s += i
    return s


print(triangle(1))
print(triangle(6))
print(triangle(215))
print(triangle(12))
