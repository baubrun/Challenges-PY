def biggerIsGreater(w):
    result = ""
    n = len(w)
    w = [i for i in w]

    idx = n - 2
    while idx >= 0 and w[idx] >= w[idx + 1]:
        idx -= 1

    if idx == -1:
        result = "no answer"    
    else:
        last_letter = n - 1
        while last_letter >= idx and w[last_letter] <= w[idx]:
            last_letter -= 1

        w[idx], w[last_letter] = w[last_letter], w[idx]
        w = "".join(w)
        result = w[:idx + 1] + w[idx + 1:][::-1]

    return result


