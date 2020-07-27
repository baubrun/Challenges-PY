def stones(n, a, b):
    result = set()
    if a > b:
        a, b = b, a


    for i in range(n):
        result.add(i * a + (n - 1 - i) * b)

    return sorted(list(result))

