"""
Given a number, return a string of the word "Boom", which varies in the following ways:

The string should include n number of "o"s, unless n is below 2 (in that case, return "boom").
If n is evenly divisible by 2, add an exclamation mark to the end.
If n is evenly divisible by 5, return the string in ALL CAPS.
If n is evenly divisible by both 2 and 5,
return the string in ALL CAPS and add an exclamation mark to the end.
The example below should help clarify these instructions.

Examples
boom_intensity(4) ➞ "Boooom!"
// There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)

boom_intensity(1) ➞ "boom"
// 1 is lower than 2, so we return "boom"

boom_intensity(5) ➞ "BOOOOOM"
// There are 5 "o"s and 5 is divisible by 5 (all caps)

boom_intensity(10) ➞ "BOOOOOOOOOOM!"
// There are 10 "o"s and 10 is divisible by 2 and 5 (all caps and exclamation mark included)
Notes
A number which is evenly divisible by 2 and 5 will have both effects applied (see example #4).
"Boom" will always start with a capital "B",
except when n is less than 2, then return a minature explosion as "boom".

"""


def boom_intensity(n):
    if n < 2:
        return "boom"
    letter_o = "o" * n
    word = "B" + letter_o + "m"
    if n % 2 == 0:
        word += "!"
    if n % 5 == 0:
        word = word.upper()
    return word


print(boom_intensity(4))
print(boom_intensity(1))
print(boom_intensity(5))
print(boom_intensity(10))
