tags = {(0, 1, 2, 3): 'R0',
        (1, 2, 3, 0): 'R90',
        (2, 3, 0, 1): 'R180',
        (3, 0, 1, 2): 'R270',
        (3, 2, 1, 0): 'V',
        (1, 0, 3, 2): 'H',
        (0, 3, 2, 1): 'D',
        (2, 1, 0, 3): "D'"}

D4 = tags.keys()


def compose(a, b):
    return tuple(a[i] for i in b)


H = {tags[compose(p, p)] for p in D4}
K = {tags[p] for p in D4 if tags[compose(p, p)] == 'R0'}

print("H = ", H)
print("K = ", K)
