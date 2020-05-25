"""
/*
Add up the Numbers from a Single Number
Create a function that takes a number as an argument. 
Add up all the numbers from 1 to the number 
you passed to the function. For example, 
if the input is 4 then your function should 
return 10 because 1 + 2 + 3 + 4 = 10.

Examples
add_up(4) ➞ 10

add_up(13) ➞ 91

add_up(600) ➞ 180300
"""
def add_up(num):
    ans = 0
    for i in range(num + 1):
        ans += i
    return ans

