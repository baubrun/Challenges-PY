"""
/*
Given an object of people and their ages, return how old the people would be after n years have passed. Use the absolute value of n.

ex:

afterNYears{
    "Joel": 32,
    "Fred": 44,
    "Reginald": 65,
    "Susan": 33,
    "Julian": 13
}
 ➞ 1 {
     "Joel": 33,
     "Fred": 45,
     "Reginald": 66,
     "Susan": 34,
     "Julian": 14
 }


Notes
Assume that everyone is immortal (it would be a bit grim 
    if I told you to remove names once they reached 75).
n should be a positive number because last time I 
checked, people don't tend to age backwards. Therefore, use the absolute value of n.
*/
"""


def ageing(name, n):
    return {k: v + abs(n) for k,v in name.items()}

afterNYears = {
    "Joel": 32,
    "Fred": 44,
    "Reginald": 65,
    "Susan": 33,
    "Julian": 13
}


# ans = ageing(afterNYears, 5)
# print(ans)