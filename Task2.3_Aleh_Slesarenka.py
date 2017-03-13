a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def compare(list_a, list_b):
    print(list(set(list_a) & set(list_b)))


compare(a, b)
