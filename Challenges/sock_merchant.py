"""
john works at a clothing store. 
He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

For example, there are 7 socks with colors ar = [1,2,1,2,1,3,2]. 
There is one pair of color 1 and one of color 2. 
There are three odd socks left, one of each color. The number of pairs is 2.
"""

s = "10 20 20 10 10 30 50 10 20".split()

s_int = [int(i) for i in s]

pairs = 0
for i in s_int:
    if i % 2 == 0:
        pairs += 1

print(pairs)