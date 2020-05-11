"""-Write a function that finds the most frequent element in an array"""


arr = [1, 2, 3, 4, 1, 5, 1, 7, 1, 6, 2, 9,9,9,9]


def most(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
        
    # return d
    mx = 0
    u = sorted(d.items(), key=lambda x: x[0])
    print(u)
    return max(u, key=lambda x: x[1])

ans = most(arr)
print("most common:", ans)
