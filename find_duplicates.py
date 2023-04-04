def find_duplicate(lst):
    filter = list()
    res = list()
    for e in lst:
        if e not in filter:
            filter.append(e)

    for e in filter:
        if e in lst:
            lst.remove(e)

    for e in filter:
        if e in lst:
            res.append(e)

    return res

assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print('OK')
