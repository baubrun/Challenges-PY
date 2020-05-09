"""
Transform Upvotes
Create a function that transforms a string of upvote counts into an array of numbers. 
Each k represents a thousand.

Examples
transformUpvotes("6.8k 13.5k") ➞ [6800, 13500]

transformUpvotes("5.5k 8.9k 32") ➞ [5500, 8900, 32]

transformUpvotes("20.3k 3.8k 7.7k 992") ➞ [20300, 3800, 7700, 992]
Notes
Return the upvotes as an array.
"""


def transformUpvotes(string):
    splited_str = string.split()
    amounts = []
    for i in splited_str:
        if i.endswith("k"):
            remoke_k_decimal = i[:-1].split(".")
            no_decimal = "".join(remoke_k_decimal)
            amounts.append(int(no_decimal) * 1000)
        else:
            amounts.append(int(i))
    return amounts


print(transformUpvotes("20.3k 3.8k 7.7k 992"))
print(transformUpvotes("5.5k 8.9k 32"))
print(transformUpvotes("6.8k 13.5k"))
