
"""
-Write l function that finds common elements
in two arrays (assume no object or nested array)
"""

def common(l1, l2):
    return [i for i in set(l1) & set(l2)]
    


a = ['l', 15978, '1', 3, 1, "asdf"]
b = ['1', 456, "LLL", "asdf", 6, 7]
ans = common(a, b)
print("common:", ans)

