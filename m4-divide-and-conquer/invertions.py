def naive_count(l):
    inv = 0
    for i, li in enumerate(l):
        for lj in l[i:]:
            if li>lj:
                inv += 1
    return inv

def dnc_count(l):
    inv, _ = sort(l)
    return inv

def sort(l):
    n = len(l)
    if n == 1:
        return 0, l
    
    a = l[:n//2]
    b = l[n//2:]

    inva, a = sort(a)
    invb, b = sort(b)
    invm, l = merge(a, b)

    return inva + invb + invm, l


def merge(a, b):
    inv, l = 0, []
    i, na = 0, len(a)
    j, nb = 0, len(b)
    if na + nb == 1:
        return 0, [*a, *b]

    while i < na and j < nb:
        ai = a[i]
        bj = b[j]
        if ai < bj:
            l.append(ai)
            i += 1
        else:
            l.append(bj)
            j += 1
            inv += na - i

    l = [*l, *a[i:], *b[j:]]
    return inv, l