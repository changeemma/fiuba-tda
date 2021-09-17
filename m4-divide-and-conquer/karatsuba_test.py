from karatsuba import split_num, join_num, karatsuba, memoized_karatsuba

def test_split_num():
    # arrange
    num = 0b11010111

    # act
    n1, n0 = split_num(n=num, l=8)

    # assert
    assert n1 == 0b1101 and n0 == 0b0111

def test_join_num():
    # arrange
    n1 = 0b1101
    n0 = 0b0111

    # act
    num = join_num(n1=n1, n0=n0, l=8)

    # assert
    assert num == 0b11010111

def test_karatsuba():
    # arrange
    x = 123456789
    y = 987654321

    # act
    r = karatsuba(x=x, y=y)
    r_memo = memoized_karatsuba(x=x, y=y)

    # assert
    assert r == r_memo == x*y

