def histogram():
    d = dict()
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d
