from invertions import naive_count, dnc_count

def test_naive_count():
    # arrange
    l1 = [2, 4, 1, 3, 5]
    l2 = [5, 4, 3, 2, 1]

    # act
    n1 = naive_count(l1)
    n2 = naive_count(l2)

    # assert
    assert n1 == 3
    assert n2 == 10

def test_dnc_count():
    # arrange
    l1 = [2, 4, 1, 3, 5]
    l2 = [5, 4, 3, 2, 1]

    # act
    n1 = dnc_count(l1)
    n2 = dnc_count(l2)

    # assert
    assert n1 == 3
    assert n2 == 10