def intersection(array1, array2):
    iter1 = iter(array1)
    iter2 = iter(array2)
    item1 = next(iter1)
    item2 = next(iter2)
    while item1 >= 0 and item2 >= 0:
        if item1 > item2:
            item2 = next(iter2, None)
            continue
        elif item1 < item2:
            item1 = next(iter1, None)
            continue
        yield item1
        item2 = next(iter2, None)
        item1 = next(iter1, None)


a = [0, 2, 2, 2, 3, 9, 9]
b = [0, 2, 3, 4, 7, 8, 9, 9, 10]
print list(intersection(a, b))
