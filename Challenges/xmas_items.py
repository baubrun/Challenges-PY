"""
On the Nth Day of Christmas...
Throughout the 12 days of Christmas, my true love gave me in total 364 items.

Create a function where given n days as an argument, return the total amount of items received throughout those days as an integer.

Examples
xmas_items(12) ➞ 364

xmas_items(3) ➞ 10

xmas_items(31) ➞ 5456
Notes
You will only be given valid inputs.
Remember to return as an integer.
0 as input should return 0.
Check the Resources tab for more information.


# xmas song verse example
On the first day of Christmas my true love sent to me
A partridge in a pear tree.

On the second day of Christmas my true love sent to me
Two turtle doves,
And a partridge in a pear tree.

On the third day of Christmas my true love sent to me
Three French hens,
Two turtle doves,
And a partridge in a pear tree....

"""


def xmas_items(n):
    l = []
    for i in range(1, n + 2):
        l.append(sum([n for n in range(i)]))
    return sum(l)


print(xmas_items(12))
print(xmas_items(3))
print(xmas_items(31))
