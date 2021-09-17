
def split_num(n, l):
    n0 = n % (1<<l//2)
    n1 = n >> l//2
    return n1, n0

def join_num(n1, n0, l):
    return (n1 << l//2) + n0


def karatsuba(x, y):
    l = max(x.bit_length(), y.bit_length())

    # base case
    if l < 2:
        return x & y
    
    # ensures odd number of bits
    l += min(l, l % 2) 
    
    x1, x0 = split_num(x, l)
    y1, y0 = split_num(y, l)

    # recursive calls
    p = karatsuba(x1 + x0, y1 + y0)
    x1y1 = karatsuba(x1, y1)
    x0y0 = karatsuba(x0, y0)

    # joining results
    return (x1y1 << l) + ((p - x1y1 - x0y0) << l//2) + x0y0


def memoized_karatsuba(x, y):
    memo = {}

    def _karatsuba(x, y):
        # prevents duplicated entries
        if x < y:
            x, y = y, x
        
        # if memoized
        if (x, y) in memo:
            return memo.get((x,y))

        l = x.bit_length()

        # base case
        if l < 2:
            return x & y
        
        # ensures odd number of bits
        l += min(l, l % 2)  
        
        x1, x0 = split_num(x, l)
        y1, y0 = split_num(y, l)

        # recursive calls
        p = _karatsuba(x1 + x0, y1 + y0) 
        x1y1 = _karatsuba(x1, y1) 
        x0y0 = _karatsuba(x0, y0) 

        # joining and registering results
        memo[(x, y)] = (x1y1 << l) + ((p - x1y1 - x0y0) << l//2) + x0y0
        return memo.get((x, y))

    return _karatsuba(x, y)

