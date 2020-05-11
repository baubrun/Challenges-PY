"""
-Write a function that removes duplicates
in an array (assume no object or nested array)
"""

def duplicates(arr):

    i = 0
    unique = []
    d = {}
    while i < len(arr) - 1:
        if arr[i] in d:
            i += 1
        else:
            d[arr[i]] = 1
            unique.append(arr[i])
            i += 1
    return unique


arr = ["a", 15978, "1", 3, 1, "a", "1", 1]

ans = duplicates(arr)
print(ans)
