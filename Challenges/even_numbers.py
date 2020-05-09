arr = [1, 2, 3, 4, 12]


def even_numbers(arr):
    return sum([i for i in arr if i % 2 == 0])

ans = even_numbers(arr)
print(ans)
