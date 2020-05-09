"""
Filter Repeating Character Strings
Create a function that keeps only strings 
with repeating identical characters (in other words, it has a set size of 1).

Examples
identical_Filter(["aaaaaa", "bc", "d", "eeee", "xyz"]) 
➞ ["aaaaaa", "d", "eeee"]

identical_Filter(["88", "999", "22", "545", "133"]) 
➞ ["88", "999", "22"]

identical_Filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"]) 
➞ []
Notes
A string with a single character is trivially counted as a 
string with repeating identical characters.
If there are no strings with repeating identical characters, 
return an empty array (see example #3).
*/
"""


def identical_Filter(arr):
    l = []
    for i in range(len(arr)):
        s = set()
        split = [l for l in arr[i]]
        s = {c for c in split}
        if len(s) == 1:
            l.append(arr[i])
    return l
    



print(identical_Filter(["88", "999", "22", "545", "133"]))
print(identical_Filter(["aaaaaa", "bc", "d", "eeee", "xyz"]))
print(identical_Filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"]))

